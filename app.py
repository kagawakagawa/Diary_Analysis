from flask import Flask, render_template, request, redirect, url_for
import csv
import os
import make_csv
import pandas as pd

app = Flask(__name__)

def read_diary_data(filename):
    data = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def append_to_csv(data, filename):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def read_csv(filename):
    data = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def write_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def edit_csv_row(data, row_index, new_values):
    if 0 <= row_index < len(data):
        data[row_index] = new_values
    else:
        print('指定された行が存在しません。')


@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/make_csv',methods=['POST'])
# 日記用にカラムがいくつか存在するCSVファイルをこのディレクトリに生成する
# 初期設定で指定したいカラムを自分で作ることができる
# def file_exists(filename):
#     return os.path.exists(filename)


def make_csv_route():
    filename = 'diary.csv'
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
    if not make_csv.file_exists(filename):
        with open(filename,mode="w",newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
            print(f'{filename} が生成されました。')
    else:
        print(f'{filename} が既に存在しています。')

    return "操作が終了しました"


@app.route('/get_user_input',methods=['POST'])
def get_user_input(): 
    A = request.form.get('A')
    B = request.form.get('B')
    C = request.form.get('C')
    D = request.form.get('D')
    E = request.form.get('E')
    F = request.form.get('F')
    G = request.form.get('G')
    H = request.form.get('H')
    I = request.form.get('I')
    J = request.form.get('J')
    K = request.form.get('K')

    data = [A, B, C, D, E, F, G, H, I, J, K]
    filename = 'diary.csv'
    
    # 既存の日記データを読み込む
    existing_data = read_diary_data(filename)
    
    # 重複をチェック
    existing_dates = [entry[0] for entry in existing_data]  # 日付だけを抽出
    if A in existing_dates:
        return "同じ日にちの日記が既に存在します。"
    
    # 重複がない場合はデータを追加して保存
    append_to_csv(data, filename)
    
    return "日記が書けましました。"


@app.route('/edit',methods=['POST'])
def edit():
    filename = 'diary.csv'
    data = read_csv(filename)

    row_index = int(request.form.get('row_index'))
    A = int(request.form.get('A'))
    B = int(request.form.get('B'))
    C = int(request.form.get('C'))
    D = int(request.form.get('D'))
    E = int(request.form.get('E'))
    F = int(request.form.get('F'))
    G = int(request.form.get('G'))
    H = int(request.form.get('H'))
    I = int(request.form.get('I'))
    J = int(request.form.get('J'))
    K = request.form.get('K')

    new_values = [A, B, C, D, E, F, G, H, I, J, K]
    edit_csv_row(data, row_index, new_values)
    write_csv(data, filename)

    return redirect(url_for('index'))

@app.route('/high_score_day_average', methods=['POST'])
def high_score_day_average():
    n_score = int(request.form['n_score'])
    
    # CSVファイルからデータを読み込む
    df = pd.read_csv('diary.csv')
    
    # ユーザーが指定した総合点以上のいい日の各項目の平均スコアを計算
    df_filtered = df[df['B'] >= n_score]


    average_list = df_filtered[['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']].mean().tolist()
    for i in range(len(average_list)):
        average_list[i] = round(average_list[i],2)
    
    return render_template('high_score_day_average.html', average_list=average_list, n_score=n_score)



@app.route('/high_score_day', methods=['POST'])
def high_score_day():
    target_score = int(request.form['target_score'])
    
    # CSVファイルからデータを読み込む
    df = pd.read_csv('diary.csv')
    
    # ユーザーが指定した点数以上のいい日の感想を取得
    high_score_feedbacks = df[df['B'] >= target_score]['K'].tolist()
    
    return render_template('high_score_day.html', high_score_feedbacks=high_score_feedbacks, target_score=target_score)

if __name__ == "__main__":
    app.run(debug=True)