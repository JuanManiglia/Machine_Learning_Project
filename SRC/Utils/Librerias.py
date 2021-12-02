import numpy as np # linear algebra
from numpy import array
from numpy import savez_compressed
from numpy import expand_dims
from numpy import zeros
from numpy import ones
from numpy import vstack
from numpy import load
from numpy.random import randint
from numpy.random import randn

import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import pandas_profiling as pp # Data Visualization

import pycaret
from pycaret.regression import *

from sklearn import preprocessing
from sklearn.model_selection import train_test_split

from pycaret.regression import *
from sklearn.preprocessing import MinMaxScaler,StandardScaler,LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from catboost import CatBoostRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import GridSearchCV
from sklearn.metrics.pairwise import cosine_similarity

import os
import datetime
import warnings
warnings.filterwarnings('ignore')
from glob import glob # se usa para recuperar archivos / nombres de ruta que coinciden con un patrón específico
import imageio # proporciona una interfaz fácil para leer y escribir una amplia gama de datos de imágenes, incluidas imágenes animadas, datos volumétricos y formatos científicos.
import PIL # agrega soporte para abrir, manipular y guardar muchos formatos de archivo de imagen
from IPython import display
from skimage.io import imread
import cv2
import time
import scipy as sp


import tensorflow as tf
from tensorflow import keras
# from tensorflow.keras.datasets.cifar10 import load_data
from tensorflow.keras import layers
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense , Reshape, Flatten, Conv2D, LeakyReLU, Dropout, Conv2DTranspose, BatchNormalization


