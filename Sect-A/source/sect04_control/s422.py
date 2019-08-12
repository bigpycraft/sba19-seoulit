num, sum = 1, 0

while True:
    sum += num
    if sum > 100:
        break
    else:
        num += 1

print('num 값이 %d 일때 while문 탈출 !!' % num)