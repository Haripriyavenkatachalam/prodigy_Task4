# -*- coding: utf-8 -*-
"""Task4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L_X5-SStNclxugEHsPyg4RetMRBx0sc8
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from textblob import TextBlob
from wordcloud import WordCloud

df = pd.read_csv('/content/sample_data/twitter_validation.csv')
df

text_df = df.drop(['id','Facebook','Irrelevant'], axis=1)
text_df.head()

text_df = text_df.drop_duplicates('text')

def polarity(text):
    return TextBlob(text).sentiment.polarity

text_df['polarity'] = text_df['text'].apply(polarity)
text_df.head(50)

# @title sentiment

from matplotlib import pyplot as plt
import seaborn as sns
text_df.groupby('sentiment').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

def sentiment(label):
    if label <0:
        return "Negative"
    elif label ==0:
        return "Neutral"
    elif label>0:
        return "Positive"
text_df['sentiment'] = text_df['polarity'].apply(sentiment)
text_df.head()

# @title sentiment vs polarity

from matplotlib import pyplot as plt
import seaborn as sns
figsize = (12, 1.2 * len(text_df['sentiment'].unique()))
plt.figure(figsize=figsize)
sns.violinplot(text_df, x='polarity', y='sentiment', inner='box', palette='Dark2')
sns.despine(top=True, right=True, bottom=True, left=True)

# @title polarity

from matplotlib import pyplot as plt
text_df['polarity'].plot(kind='hist', bins=20, title='polarity')
plt.gca().spines[['top', 'right',]].set_visible(False)