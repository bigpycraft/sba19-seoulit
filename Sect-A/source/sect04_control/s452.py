# 2단에서 9단까지 출력

# 단은 몇바퀴? 2~9단까지니깐 8바퀴
# 단안에 계산은 9바퀴

for dan in range(2, 10):
    print(dan , '단')

    for num in range(1, 10):
        gop = dan * num

        print(dan, 'x', num, '=', gop)

    print("-"*10)

print("구구단 종료!!")
