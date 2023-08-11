import sqlite3
import os

# データベース接続とテーブル作成
db_filename = "made_memo.db"
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS memos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT
    )
''')
conn.commit()

def add_memo(content):
    cursor.execute("INSERT INTO memos (content) VALUES (?)", (content,))
    conn.commit()

def get_memos():
    cursor.execute("SELECT * FROM memos")
    return cursor.fetchall()

# メモを保存
memo_content = input("Enter your memo: ")
add_memo(memo_content)

# メモを表示
memos = get_memos()
print("\nYour memos:")
for memo in memos:
    print(memo[0], memo[1])

# データベース接続を閉じる
conn.close()
