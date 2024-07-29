# Sentiment Analysis(main.py) without NLTK

This project performs sentiment analysis on a given text file. It processes the text to identify and count emotional words, and then visualizes the results in a bar graph showing the distribution of different emotions.

## Key Features

- **Text Preprocessing**: Converts text to lowercase, removes special characters, and tokenizes words.
- **Stop Words Removal**: Eliminates common stop words that do not contribute to the sentiment analysis.
- **Emotion Detection**: Identifies and counts words associated with specific emotions.
- **Visualization**: Plots a bar graph of the emotions detected in the text.

## Requirements

- Python 3.x
- Matplotlib

## Setup

1. **Install Dependencies**

   Ensure you have the necessary Python packages installed. You can install them using pip:

   ```bash
   pip install matplotlib
Prepare the Text Files

read.txt: The input text file containing the text to be analyzed.
emotion.txt: A file mapping words to emotions. Each line should be in the format: word:emotion.
Code Overview
1. Text Preprocessing
Lowercase Conversion: Converts the text to lowercase to ensure uniformity.
Special Character Removal: Removes punctuation and special characters from the text.
Tokenization: Splits the text into individual words.
2. Stop Words Removal
Stop Words: Common words that do not add significant meaning to the text are removed.
3. Emotion Detection
Emotion Mapping: Reads the emotion.txt file and maps words in the text to corresponding emotions.
Count Emotions: Uses collections.Counter to count the frequency of each emotion.
4. Visualization
Matplotlib: Plots a bar graph showing the frequency of each detected emotion.
Usage
Run the Script

Execute the script to perform sentiment analysis on the text in read.txt:

bash
python sentiment_analysis.py
View the Results

The script will save a bar graph (graph.png) visualizing the distribution of emotions.


# Sentiment Analysis(main2.py) with NLTK

This project performs sentiment analysis on a given text file. It processes the text to identify and count emotional words, and then uses the NLTK VADER sentiment analyzer to determine the overall sentiment (positive, negative, or neutral) of the text. The results are visualized in a bar graph showing the distribution of different emotions.

## Key Features

- **Text Preprocessing**: Converts text to lowercase, removes special characters, and tokenizes words.
- **Stop Words Removal**: Eliminates common stop words that do not contribute to the sentiment analysis.
- **Emotion Detection**: Identifies and counts words associated with specific emotions.
- **Sentiment Analysis**: Uses VADER sentiment analysis to classify the text as positive, negative, or neutral.
- **Visualization**: Plots a bar graph of the emotions detected in the text.

## Requirements

- Python 3.x
- NLTK
- Matplotlib

## Setup

1. **Install Dependencies**

   Ensure you have the necessary Python packages installed. You can install them using pip:

   ```bash
   pip install nltk matplotlib
Download NLTK Data

You need to download the stopwords and VADER lexicon data:

python
Copy code
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('vader_lexicon')
Prepare the Text Files

read.txt: The input text file containing the text to be analyzed.
emotion.txt: A file mapping words to emotions. Each line should be in the format: word:emotion.
Code Overview
1. Text Preprocessing
Lowercase Conversion: Converts the text to lowercase to ensure uniformity.
Special Character Removal: Removes punctuation and special characters from the text.
Tokenization: Splits the text into individual words.
2. Stop Words Removal
Stop Words: Common words that do not add significant meaning to the text are removed.
3. Emotion Detection
Emotion Mapping: Reads the emotion.txt file and maps words in the text to corresponding emotions.
Count Emotions: Uses collections.Counter to count the frequency of each emotion.
4. Sentiment Analysis
VADER Sentiment Analysis: Analyzes the text to determine the overall sentiment score.
5. Visualization
Matplotlib: Plots a bar graph showing the frequency of each detected emotion.
Usage
Run the Script

Execute the script to perform sentiment analysis on the text in read.txt:

bash
Copy code
python sentiment_analysis.py
View the Results

The script will output the overall sentiment (positive, negative, or neutral) and save a bar graph (graph.png) visualizing the distribution of emotions.
License
This project is licensed under the MIT License - see the LICENSE file for details.
