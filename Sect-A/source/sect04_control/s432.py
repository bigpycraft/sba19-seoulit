# break vs. continue vs. pass
scope = list(range(1, 100))

for num in scope:

    if num <= 10:
        if num % 2 == 0:
            pass
            print(num, 'is even number.')
        else:
            continue
            print(num, 'is odd number.')
    else:
        print(num, 'is bigger than ten')
        break
        print('after break')

print('프로그램을 종료합니다.')
