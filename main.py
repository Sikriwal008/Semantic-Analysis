import string
from collections import  Counter
import matplotlib.pyplot as plt

text=open('read.txt',encoding='utf-8').read()
# converting upper to lower case
lower_case=text.lower()
# remove special character
cleaned_text=lower_case.translate(str.maketrans("","",string.punctuation))

# convert the cleaned_text into the list
tokanized_word=cleaned_text.split()

# remove the stop words:-the words which does not add any meaning to the sentence is called as stop words
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Removing stop words from the tokenized words list
final_words = []
for word in tokanized_word:
    if word not in stop_words:
        final_words.append(word)
# print(final_words)

# import the emotion file
final_ewmotion=[]
with open('emotion.txt','r') as file:
    for line in file:
        clear_line=line.replace("\n",'').replace(",",'').replace("'",'').strip()
        word,emotionn=clear_line.split(':')
        # print('Word:'+word+" "+"Emotion:"+emotionn)

        if word in final_words:
            final_ewmotion.append(emotionn)

# count the emotional words
w=Counter(final_ewmotion)
fig,axl=plt.subplots()
axl.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()

# print(w)