# 
## Librerias

import sys 
import os  # obtener el path del jupyter tenemos esto 
os.chdir(os.path.dirname(__file__))
from Utils.Librerias import *
from Utils.Path import *
from Utils.Visualizacion import *
from Utils.Limpieza import *
import pickle
cf.go_offline()


## Carga de Datos

MAL = pd.read_csv(AnimeList)

## Limpieza de Dataset

def Modelo_def(MAL):

    MAL = MAL[['title', 'type', 'source', 'rating', 'score', 'scored_by', 'rank', 'popularity', 'members', 'favorites', 'aired_string']]
    MAL.dropna(inplace = True) 
    aired_to_year(MAL,'aired_string')
    only_year(MAL,'Year_Aired')
    MAL = MAL.drop(['aired_string', 'Year_Aired'], axis=1)
    MAL = MAL.drop(MAL[MAL['Year'] == 'Unknown'].index)
    MAL['type'] = MAL['type'].map({'TV': 0, 'Music': 1, 'OVA': 2, 'ONA': 3, 'Special': 4, 'Movie': 5})
    MAL['source'] = MAL['source'].map({'Manga': 0, 'Original': 1, 'Light novel': 2, '4-koma manga': 3, 'Novel': 4, 'Visual novel': 5, 
                                    'Unknown': 6, 'Other': 7, 'Music': 8, 'Game': 9, 'Picture book': 10, 'Card game': 11, 
                                    'Web manga': 12, 'Book': 13, 'Radio': 14, 'Digital manga': 15})
    MAL['rating'] = MAL['rating'].map({'PG-13 - Teens 13 or older': 0, 'PG - Children': 1, 'G - All Ages': 2, 'R+ - Mild Nudity': 3, 
                                    'R - 17+ (violence & profanity)': 4, 'None': 5, 'Rx - Hentai': 6})
    MAL['Year'] = MAL['Year'].astype(int)

    X = MAL.drop(['title', 'score', 'rank'], axis=1)
    y = MAL[['score']]
    X_train, X_test, y_train, y_test = train_test_split(
                                                    X, 
                                                    y, 
                                                    test_size=0.20, 
                                                    random_state=42)

    model = RandomForestRegressor(bootstrap=True, ccp_alpha=0.0, criterion='mse',
                      max_depth=None, max_features='auto', max_leaf_nodes=None,
                      max_samples=None, min_impurity_decrease=0.0,
                      min_impurity_split=None, min_samples_leaf=1,
                      min_samples_split=2, min_weight_fraction_leaf=0.0,
                      n_estimators=100, n_jobs=-1, oob_score=False,
                      random_state=123, verbose=0, warm_start=False)

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print('MAE:', mean_absolute_error(y_test, predictions))
    print('MSE:', mean_squared_error(y_test, predictions))
    print('RMSE:', np.sqrt(mean_squared_error(y_test, predictions)))
    print('R2 Score:', r2_score(y_test, predictions))
    print('La metrica que vamos a tomar mas encuenta es el MAE, porque nos instereza que tenga la minima diferencia con respecto al original')

def save_model(model):

    filename = 'finished_model'
    with open(filename, 'wb') as archivo_salida:
        pickle.dump(model, archivo_salida)


Modelo_def(MAL)
# save_model(model)