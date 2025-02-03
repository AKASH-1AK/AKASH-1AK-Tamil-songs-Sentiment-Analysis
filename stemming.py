from tamil import vaaninlp
from collections import Counter
import string
text = open('tamil.txt',encoding='utf-8').read()
cleaned_text = text.translate(str.maketrans('','',string.punctuation))
sol = vaaninlp.word_tokenize(cleaned_text)
sorkal = vaaninlp.lemmatize(sol)
for i in range(len(sorkal)):
  if(sorkal[i]["Flag"]==True):
     print(sorkal[i]["Userword"]+" ->  "+ ",".join( list(dict.fromkeys(sorkal[i]["RootWords"]))))
  else:
    print(sorkal[i]["Userword"]+" ->  <தெரியவில்லை>")
emotion_list=[]

with open('emotion1.txt','r')as file:
        if word in sorkal:
            emotion_list.append(emotion)
print(emotion_list)