import pandas as pd

# Excelファイルのパス
excel_file_path = 'diary.xlsx'

# 読み込むシートの名前またはインデックス（0から始まる）
sheet_name = 'Sheet1'

# ExcelファイルをDataFrameに読み込む
df = pd.read_excel(excel_file_path, sheet_name)

# CSVファイルに保存
csv_file_path = 'diary.csv'
df.to_csv(csv_file_path, index=False, encoding='utf-8')

print(f'Excelファイル "{excel_file_path}" をCSVファイル "{csv_file_path}" に変換しました。')
