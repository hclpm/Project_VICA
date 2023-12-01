import os.path
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import seaborn as sns

from pathlib import Path
from tqdm import tqdm
from time import perf_counter

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,accuracy_score
from IPython.display import Markdown, display

# training data location
dir_ = Path('C:/Users/js2-3/Desktop/Github/Desktop_sync/Projects/Communication_Assistant/VideoCall/Portrait')
filepaths = list(dir_.glob(r'**/*.jpg'))

# labeling
def proc_img(filepath):
    labels = [str(filepath[i]).split("\\")[-1].split("_")[0] for i in range(len(filepath))]

    filepath = pd.Series(filepath, name='Filepath').astype(str)
    labels = pd.Series(labels, name='Label')

    # 경로와 라벨 concatenate
    df = pd.concat([filepath, labels], axis=1)

    # index 재설정
    df = df.sample(frac=1,random_state=0).reset_index(drop = True)
    
    return df

df = proc_img(filepaths)
print(df["Filepath"].head(3))