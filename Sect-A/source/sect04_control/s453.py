# 화면에 300개의 세로 선을 긋는다

# 그래픽 라이브러리를 도입한다
from tkinter import *
# 화면 초기화
w = Canvas(Tk(), width=900, height=400)
w.pack()

# 선을 많이 긋는다 ---- (*1)
for i in range(300):
    x = i * 3
    w.create_line(x, 0, x, 400, fill="#FF0000")

mainloop()

