from tamil import vaaninlp
from collections import Counter
import matplotlib.pyplot as plt

# Read input Tamil text
try:
    text = open('tamil.txt', encoding='utf-8').read()
    print("Input Text Length:", len(text))
    print("Input Text Content:", repr(text))
except Exception as e:
    print("Error reading tamil.txt:", e)
    text = ""

# Tokenize words
sorkal = vaaninlp.word_tokenize(text)
print("Tokenized Words (sorkal):", sorkal)

# Remove stopwords (Handle errors)
try:
    sw_removed = vaaninlp.remove_stopwords(sorkal)
    print("Stopwords Removed:", sw_removed)
except Exception as e:
    print("Error while removing stopwords:", e)
    sw_removed = sorkal

# Extract root words (only if tokenization succeeded)
if sorkal:
    try:
        root_words = vaaninlp.get_entities(sorkal)
        print("Root Words:", root_words)
    except Exception as e:
        print("Error extracting root words:", e)
else:
    root_words = []

# Lemmatization
try:
    lemm = vaaninlp.lemmatize(sorkal)
    lemm_roots = [
        ",".join(list(dict.fromkeys(item["RootWords"])))
        for item in lemm if item.get("Flag", False)
    ]
    print("Lemmatized Root Words:", lemm_roots)
except Exception as e:
    print("Error during lemmatization:", e)
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
    print("Matched Emotions:", emotion_list)
except Exception as e:
    print("Error reading emotion1.txt:", e)

# Count emotions
w = Counter(emotion_list)
print("Emotion Counts:", w)

# Generate bar graph
if w:
    emotions = list(w.keys())
    counts = list(w.values())

    plt.figure(figsize=(8, 5))
    plt.bar(emotions, counts, color='skyblue', edgecolor='black')
    plt.title("Emotion Analysis in Tamil", fontsize=16)
    plt.xlabel("Emotions", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.tight_layout()
    plt.show()
else:
    print("No emotions to display in the graph.")
