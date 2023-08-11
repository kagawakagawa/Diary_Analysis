# 日記用にカラムがいくつか存在するCSVファイルをこのディレクトリに生成する
# 初期設定で指定したいカラムを自分で作ることができる
import csv
import os

def file_exists(filename):
    return os.path.exists(filename)

data = [
    ['A','B','C','D','E','F','G','H','I','J','K'],
    # A:日にち
    # B:全体の点数
    # C:よく笑った
    # D:よく起こった
    # E:人とたくさん話した
    # F:一人でいる時間が多かった
    # G:考える時間が多かった
    # H:直感で動くことが多かった
    # I:何かを発見できた
    # J:何かを反省できた
    # K:自由記述欄
]

filename = 'diary.csv'

def make_csv():
    if not file_exists(filename):
        with open(filename,mode="w",newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
            print(f'{filename} が生成されました。')
    else:
        print(f'{filename} が既に存在しています。')



