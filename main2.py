import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import  Counter
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

text=open('read.txt',encoding='utf-8').read()
# converting upper to lower case
lower_case=text.lower()
# remove special character
cleaned_text=lower_case.translate(str.maketrans("","",string.punctuation))

# convert the cleaned_text into the list
tokanized_word=word_tokenize(cleaned_text,"english")

# remove the stop words:-the words which does not add any meaning to the sentence is called as stop words

# Removing stop words from the tokenized words list
final_words = []
for word in tokanized_word:
    if word not in stopwords.words('english'):
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

# analyse the sentiment if it gives positive vives or Negataive vives
def sentime_analyser(sentiment_text):
    score=SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    # print(score)
    neg=score['neg']
    pos=score['pos']

    if pos>neg:
        print("Positive Sentiment")
    elif pos<neg:
        print("Negative Sentiment")
    else:
        print("Neutral Sentiment ")

sentime_analyser(cleaned_text)
fig,axl=plt.subplots()
axl.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()

# print(w)