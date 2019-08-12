# 빨간색과 파란색을 교대로 100개 긋는다

# 그래픽 라이브러리를 도입한다
from tkinter import *
# 화면 초기화
w = Canvas(Tk(), width=900, height=400)
w.pack()

# 선을 교대로 많이 긋는다 ---- (*1)
for i in range(100):
    x = i * 9 
    if i % 2 == 0:
        c = "#ff0000"
    else:
        c = "#0000FF"
    w.create_line(x, 0, x, 400, fill=c)

mainloop()

