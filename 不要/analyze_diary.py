# 日記を読み込んで分析ができる
import csv
import os
import pandas as pd
import numpy as np

filename = 'diary.csv'
df = pd.read_csv(filename)

# 任意の点数を超える日の日記の任意のカラムを出力
def high_score_day(df):
    high_score_day_list = []
    n = 80
    column = 10
    for index,row in df.iterrows():
        if row[1] > n:
            high_score_day_list.append(row)
    print(len(high_score_day_list))
    for row in high_score_day_list:
        print(row[column])
        

def high_score_day_average(df):
    '''
    点数が高かった日のそれぞれの項目の平均点を見ることで
    自分が何に満足しているのか判断できる
    自分が知らない自分を簡単に見ることができる
    '''

    total_list = [0]*8 # 八個の要素のリストを作成、それぞれに合計をぶち込む
    n = 0
    n_score = 80
    for index,row in df.iterrows():
        if row[1] > n_score: # 70以上なら149
            for i in range(len(row)):
                #0,1は無視
                if i >= 2 and i <= 9:
                    #total_list.append(row[i])
                    total_list[i - 2] += row[i]
                #colum_name = str(i)
                #total_list[i-2] += row[colum_name]
            n += 1

    average_list = [i / n for i in total_list]
    for i in range(len(average_list)):
        average_list[i] = round(average_list[i],2)
    



    print('1日の総合点が' + str(n_score) + '点以上での各要素の平均点')
    print('よく笑った　　　　　　　:' + str(average_list[0]))
    print('よく怒った　　　　　　　:' + str(average_list[1]))
    print('人とたくさん話した　　　:' + str(average_list[2]))
    print('一人でいる時間が多かった:' + str(average_list[3]))
    print('考える時間が多かった　　:' + str(average_list[4]))
    print('直感で動くことが多かった:' + str(average_list[5]))
    print('発見できた　　　　　　　:' + str(average_list[6]))
    print('反省できた　　　　　　　:' + str(average_list[7]))
   
    




high_score_day(df)
print()
high_score_day_average(df)


