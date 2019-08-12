#pass 문 예시

signals = 'blue', 'yellow', 'red'

for x in range(len(signals)):
    print(x, signals[x], '루프 시작!')
    if signals[x] == 'yellow':
        pass
    print(x, signals[x], '루프 종료!!')

print('프로그램 종료!!!')
