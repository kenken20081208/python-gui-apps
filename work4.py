import tkinter as tk
import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

# リスト
meibo = []


def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    meibo.append(entry1.get())
    name_list = ""
    for a in meibo:
        name_list += f"{a}\n"  # 入力値を取得
    label1.config(text=f"{name_list}\n ")  # 画面に出力


# リストの中からランダムに一つ要素を取り出す
def button_action2():
    a = random.choice(meibo)
    label2.config(text=a)


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="追加", command=button_action)
button1.pack(pady=10)
# ボタン2
button2 = tk.Button(window, text="ランダム選択", command=button_action2)
button2.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)
label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label2.pack(pady=10)


# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
