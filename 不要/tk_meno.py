import tkinter as tk
import tkinter.filedialog

root = tk.Tk()

# テキストボックスを作成する
text_widget = tk.Text(root, wrap=tk.CHAR)
text_widget.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

# テキストボックスの大きさを可変にする
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

def save_file_as(event=None):
    """名前を付けて保存する"""
    f_type = [('Text', '*.txt')]

    file_path = tkinter.filedialog.asksaveasfilename(
        filetypes=f_type)

    if file_path != "":
        with open(file_path, "w") as f:
            f.write(text_widget.get("1.0", "end-1c"))

    return

root.bind('<Control-KeyPress-s>', save_file_as)

# 作成したメモの保存
# 保存場所はmemo_dbで

tk.Button(root, text="Save", command=save_file_as())
        

root.title("日記")
root.geometry("500x250")
root.mainloop()