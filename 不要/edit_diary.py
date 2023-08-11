import csv

filename = 'diary.csv'

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

def main():
    data = read_csv(filename)
    print('現在のデータ:')
    for index, row in enumerate(data):
        print(f'{index}: {row}')

    row_index = int(input('編集する行の番号を入力してください: '))
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

    new_values = [A,B,C,D,E,F,G,H,I,J,K]
    edit_csv_row(data, row_index, new_values)
    write_csv(data, filename)

    print('データが編集されました。')

if __name__ == '__main__':
    main()
