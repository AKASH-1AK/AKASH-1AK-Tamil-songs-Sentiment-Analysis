import streamlit as st
from tamil import vaaninlp
from collections import Counter
import matplotlib.pyplot as plt
from warnings import filterwarnings

# Streamlit app title
st.title("Tamil Song Emotion Analysis")

# Upload file
uploaded_file = st.file_uploader("Upload a Tamil text file", type=["txt"])
if uploaded_file is not None:
    # Read the uploaded file
    text = uploaded_file.read().decode("utf-8")

    # Tokenize words
    sorkal = vaaninlp.word_tokenize(text)

    # Remove stopwords
    try:
        sw_removed = vaaninlp.remove_stopwords(sorkal)
    except Exception as e:
        st.error(f"Error while removing stopwords: {e}")
        sw_removed = sorkal

    # Lemmatization
    try:
        lemm = vaaninlp.lemmatize(sorkal)
        lemm_roots = [
            ",".join(list(dict.fromkeys(item["RootWords"])))
            for item in lemm if item.get("Flag", False)
        ]
    except Exception as e:
        st.error(f"Error during lemmatization: {e}")
        lemm_roots = []

    # Match emotions
    emotion_list = []
    try:
        with open('emotion1.txt', 'r', encoding='utf-8') as file:
            for line in file:
                clear_line = line.replace('\n', '').replace(",", '').replace("\"", '').replace(' ', '').strip()
                if ':' in clear_line:
                    word, emotion = clear_line.split(':')
                    if word in lemm_roots:
                        emotion_list.append(emotion)
    except Exception as e:
        st.error(f"Error reading emotion1.txt: {e}")

    # Count emotions
    w = Counter(emotion_list)

    # Generate bar graph
    if w:
        emotions = list(w.keys())
        counts = list(w.values())

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(emotions, counts, color='skyblue', edgecolor='black')
        ax.set_title("Emotion Analysis in Tamil", fontsize=16)
        ax.set_xlabel("Emotions", fontsize=12)
        ax.set_ylabel("Count", fontsize=12)
        plt.xticks(rotation=45, fontsize=10)
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.write("No emotions detected in the text.")
else:
    st.write("Please upload a Tamil text file to proceed.")