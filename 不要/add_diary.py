import csv

filename = 'diary.csv'

def get_user_input(): 
    A = int(input("今日の日にちを入力してください(例 20230809): "))
    B = int(input("今日の点数を入力してください: "))
    print("1~5で評価してください")
    C = int(input("よく笑いましたか"))
    D = int(input("よく怒りましたか"))
    E = int(input("人とたくさん話しましたか"))
    F = int(input("一人でいる時間が多かったですか"))
    G = int(input("考える時間は多かったですか"))
    H = int(input("直感で動くことが多かったですか"))
    I = int(input("何かを発見できましたか"))
    J = int(input("何かを反省できましたか"))
    K = input("自由記述欄です")
    return [A,B,C,D,E,F,G,H,I,J,K]

def append_to_csv(data, filename):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

while True:
    new_data = get_user_input()
    append_to_csv(new_data, filename)
    
    another_entry = input("続けますか？ (y/n): ")
    if another_entry.lower() != 'y':
        break

print('データの追記が完了しました。')
