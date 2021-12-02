import seaborn as sns
import matplotlib.pyplot as plt
import plotly as py
import cufflinks as cf
import plotly.express as px
import plotly.graph_objs as go
from wordcloud import WordCloud
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot, init_notebook_mode

def data_bar(df):
    plt.figure(figsize = (15, 5))
    sns.countplot(x = 'source', data = df)
    return plt.show();

def data_countplot(df):
    plt.figure(figsize = (150, 50))
    sns.countplot(x = 'score', data = df)
    plt.xlabel('score')
    return plt.show();

def top_10_bar(df):
    
    combine_anime_rating = df.dropna(axis = 0, subset = ['title'])
    anime_ratingCount = (combine_anime_rating.groupby(by = ['title'])
    ['rating_user'].count().reset_index().rename(columns = 
    {'rating': 'totalRatingCount'})[['title', 'rating_user']])
    top10_animerating=anime_ratingCount[['title', 'rating_user']].sort_values(by = 'rating_user',ascending = False).head(10)
    fig, ax = plt.subplots(figsize = (9, 3))
    ax=sns.barplot(x="title", y="rating_user", data=top10_animerating, palette="Dark2")
    ax.set_xticklabels(ax.get_xticklabels(), fontsize=11, rotation=40, ha="right")
    ax.set_title('Top 10 Anime',fontsize = 22)
    ax.set_xlabel('Anime',fontsize = 20) 
    ax.set_ylabel('User Rating count', fontsize = 20)