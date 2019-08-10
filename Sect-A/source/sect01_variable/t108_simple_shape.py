import turtle

turtle.pensize(10)

# 사각형 그리기
input('엔터를 치면 사각형을 그립니다.')

turtle.color("red")
turtle.forward(200)

turtle.left(90)
turtle.forward(200)

turtle.left(90)
turtle.forward(200)

turtle.left(90)
turtle.forward(200)

# turtle.done()

# 삼각형 그리기
input('엔터를 치면 빨간색 삼각형을 그립니다.')

turtle.color("green")

turtle.right(30)
turtle.forward(300)

turtle.left(120)
turtle.forward(300)

turtle.left(120)
turtle.forward(300)

# turtle.done()

# 원그리기
input('엔터를 치면 파란색 굵은 원을 그립니다.')

turtle.right(30)
turtle.color("blue")
turtle.circle(200)

turtle.done()
