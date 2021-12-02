import pandas as pd
import numpy as np

def genero(df):
    
    """"
    Función que crea columnas con 0 ó 1 si la serie contiene ese genero

    """

    generes = ['Action', 'Adventure', 'Cars', 'Comedy', 'Dementia', 'Demons', 
            'Drama', 'Ecchi', 'Fantasy', 'Game', 'Harem', 'Hentai', 'Historical',
            'Horror', 'Josei', 'Kids', 'Magic', 'Martial Arts', 'Mecha',
            'Military', 'Music', 'Mystery', 'Parody', 'Police', 'Psychological',
            'Romance', 'Samurai', 'School', 'Sci-Fi', 'Seinen', 'Shoujo',
            'Shoujo Ai', 'Shounen', 'Shounen Ai', 'Slice of Life', 'Space',
            'Sports', 'Super Power', 'Supernatural', 'Thriller', 'Vampire',
            'Yaoi', 'Yuri']

    for g in generes:
            
        df[g] = df['genre'].str.contains(g)
        df[g] = df[g].astype(bool)
        df[g] = df[g].astype(int)
    anime_genres_set = list(map(str, (df['genre'])))
    return df

def aired_to_year(df,columna):

    """
    Crea una columna que en el dataframe tomando solo el a#o que
    fue lanzado al aire la serie

    """

    lista = []
    for i in df[columna]:
        lista.append(i+'\n')
    dates = []
    for x in df[columna]:
        if 'to' in x:
            dates.append(x.split(R' to'))
        else:
            dates.append(x)
    Year_aired = []
    for y in dates:
        if isinstance(y, list):
            from_value = y[0]
            Year_aired.append(from_value)
        elif isinstance(y, str):
            from_value = y
            Year_aired.append(from_value)
    df['Year_Aired'] = Year_aired
    return df
        
def only_year (df,columna):
    
    """
    Crea una Columna solo con el a#o, de cuando la serie salió al aire 

    """

    lista_year = []
    for i in df[columna]:
        if ',' in i:
            lista_year.append(i.split(R', '))
        else:
            lista_year.append(i)
    Year = []
    for x in lista_year:
        try:
            if isinstance(x, list):
                from_value = int(x[1])
                Year.append(from_value)
            elif isinstance(x, str):
                from_value = int(x)
                Year.append(from_value)
        except:
            Year.append('Unknown')
    df['Year'] = Year
    return df

def Clean_MAL(df):

    """
    Hace los cambios necesarios para transformar el dataframe en uno utilizable
    reemplazando algunos elementos, eliminado los unknown y null, y para terminar
    hace un reseteo del index

    """

    df['source'].replace(['4-koma manga', 'Web manga', 'Digital manga'], 'Manga', inplace = True)
    df['source'].replace(['Picture book', 'Card game', 'Music', 'Radio'], 'Other', inplace = True)
    df['source'].replace(['Novel', 'Book'], 'Novel', inplace = True)
    df = df[df['type'] != 'Music']
    df = df[df['source'] != 'Unknown']
    df = df[pd.notnull(df['genre'])]
    df = df[df['Year'] != 'Unknown']
    df.drop(['aired_string', 'Year_Aired', 'title_english', 'title_japanese', 
        'title_synonyms', 'image_url','airing', 'aired', 'background', 
        'premiered', 'broadcast', 'related', 'producer', 'licensor', 
        'opening_theme', 'ending_theme'], axis=1, inplace=True)
    df.reset_index(drop = True, inplace = True)

    return df

def Clean_MAL_User(df):
    
    """
    Transformar el dataframe en uno utilizable eliminado los unknown y null, 
    y para terminar hace un reseteo del index

    """
    
    df['my_rewatching'] = df['my_rewatching'].fillna(0)
    MAL_User = df[pd.notnull(df['username'])]
    MAL_User.drop(['my_watched_episodes', 'my_start_date', 'my_finish_date', 
                    'my_last_updated', 'my_rewatching_ep', 'my_tags'], 
                    axis=1, inplace = True)
    MAL_User.reset_index(drop = True, inplace = True)

    return MAL_User

def Clean_MAL_Rating(df):

    """
    Cambia a NAN los rating con -1

    """
    df['rating'] = df['rating'].apply(lambda x: np.nan if x==-1 else x)
    
    return df

def rating(df):
    
    combine_anime_rating = df.dropna(axis = 0, subset = ['title'])
    MAL_Rating_Count = (combine_anime_rating.groupby(by = ['title'])
    ['rating_user'].count().reset_index().rename(columns = 
    {'rating': 'totalRatingCount'})[['title', 'rating_user']])

    return MAL_Rating_Count