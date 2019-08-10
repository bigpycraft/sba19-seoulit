import turtle
import time

input ('엔터를 치면 거북이를 소개합니다.^^')

turtle.shape('turtle')

print('앞으로 전진합니다.')
time.sleep(1)
turtle.forward(100)

print('한번더 앞으로 전진합니다.')
time.sleep(1)
turtle.forward(100)

print('왼쪽으로 전진합니다.')
time.sleep(1)
turtle.left(90)
turtle.forward(100)

print('오른쪽으로 전진합니다.')
time.sleep(1)
turtle.right(90)
turtle.forward(100)

turtle.done()