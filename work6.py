import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑


def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    # user_input = entry1.get()
    label1.config(text=f"")  # 画面に出力


# 入力フィールドの作成
# entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
# entry1.grid(column=7, row=4, pady=10)

# pady君が上下
# padx君が左右

# ボタンの作成
button1 = tk.Button(window, text="Submit", command=button_action)
button1.grid(column=6, row=3, padx=10)

button2 = tk.Button(window, text="Submit", command=button_action)
button2.grid(column=6, row=5, padx=10)

button3 = tk.Button(window, text="Submit", command=button_action)
button3.grid(column=6, row=7, padx=10)
# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.grid(column=6, row=9, padx=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
