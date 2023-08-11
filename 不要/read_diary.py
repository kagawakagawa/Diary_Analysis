# 日記を読み込んで任意のカラムを抽出する
import csv
import os
import pandas as pd
import numpy as np

filename = 'diary.csv'
df = pd.read_csv(filename)

columA = df['A']
columC = df['C']

print(columA)
print('よく笑ったか')
print(columC)
