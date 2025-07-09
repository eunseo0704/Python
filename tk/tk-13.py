from tkinter import *

window = Tk()
Label(window, text="이름").grid(row=0)  # 테이블의 0번째 행
Label(window, text="나이").grid(row=1)  # 테이블의 1번째 행

e1 = Entry(window)
e2 = Entry(window)

e1.grid(row=0, column=1)    # 콤마(,)로 구분
e2.grid(row=1, column=1)    # 여기도 row=1로 수정해야 맞음

window.mainloop()
