# numbers = list(range(10))
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('numbers :', numbers)
idx, sum = 0, 0

while idx < len(numbers):
    num = numbers[idx]
    sum += num
    idx += 1

print('numbers의 합계는 %d 입니다.' % sum)

