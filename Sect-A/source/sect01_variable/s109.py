import turtle

# 사각형 그리기 응용
size  = input('사각형의 크기를 입력하세요.[100~300] ')
color = input('선의 색깔을 입력하세요.[red / green / blue]  ')
thick = input('펜의 굵기를 입력하세요.[1~30]   ')

angle = 90
thick = int(thick)
size  = int(size)

turtle.color(color)
turtle.pensize(thick)

turtle.left(angle)
turtle.forward(size)

turtle.left(angle)
turtle.forward(size)

turtle.left(angle)
turtle.forward(size)

turtle.left(angle)
turtle.forward(size)

turtle.done()

