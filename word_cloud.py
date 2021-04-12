import nltk
from nltk.stem.api import StemmerI
from nltk.tag.brill import Word
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
import pandas as pd
import re

from wordcloud import WordCloud, STOPWORDS
nltk.download('punkt')


def data_cleaning(text:str) -> str:
    """
    Cleaning the urls,mentions,hashtags
    """
    text = re.sub(r"http\S+", "", text) #remove urls
    text=re.sub(r'\S+\.com\S+','',text) #remove urls
    text=re.sub(r'\@\w+','',text) #remove mentions
    text =re.sub(r'\#\w+','',text) #remove hashtags
    return text

def data_processing(text:str, stem=False):
    """
    Tokenizing the cleaned text and all
    """
    # stemmer = StemmerI()
    text=data_cleaning(text)
    text = re.sub('[^A-Za-z]', ' ', text.lower()) #remove non-alphabets
    tokenized_text = word_tokenize(text) #tokenize
    clean_text = [word for word in tokenized_text]
    # if stem:
    #     clean_text=[stemmer(word) for word in clean_text]
    return ' '.join(clean_text)



def make_word_cloud(text_list:list,width:int,height:int,color:str):
    """
    takes the list if texts and forms a text cloud and 
    use plt.save("") to save the media file.
    """
    text = ' '.join(text_list)
    cloud = WordCloud(width=width,height=height,background_color=color,
                    min_font_size=10).generate(text)
    cloud.to_file("fig1.png")

def start_cloud(df:pd.DataFrame) -> None:
    """
    Think this as main function where you get tweets dataframe.
    """
    df["cleaned_text"] = df["text"].apply(lambda x: data_cleaning(x))
    df["cleaned_text"] = df["cleaned_text"].apply(lambda x: data_processing(x))
    text_list = df["cleaned_text"].to_list()
    width = 800
    height = 800
    color = 'white'
    make_word_cloud(text_list,width,height,color)
    return "fig1.png"