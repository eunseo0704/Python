import tkinter as tk

root = tk.Tk()
root.title("여러 버튼 배치 예제")
root.geometry("300x200")

btn_1 = tk.Button(root, text="1")
btn_2 = tk.Button(root, text="2")
btn_3 = tk.Button(root, text="3")
btn_4 = tk.Button(root, text="4")
btn_6 = tk.Button(root, text="6")
btn_7 = tk.Button(root, text="7")
btn_8 = tk.Button(root, text="8")
btn_11 = tk.Button(root, text="11")
btn_12 = tk.Button(root, text="12")

btn_1.grid(row=0, column=0, sticky="news")
btn_2.grid(row=0, column=1, sticky="news")
btn_3.grid(row=0, column=2, sticky="news")
btn_4.grid(row=1, column=0, columnspan=2, sticky="news")
btn_6.grid(row=1, column=2, sticky="news")
btn_7.grid(row=2, column=0, rowspan=2, sticky="news")
btn_8.grid(row=2, column=1, columnspan=2, sticky="news")
btn_11.grid(row=3, column=1, sticky="news")
btn_12.grid(row=3, column=2, sticky="news")

root.mainloop()
