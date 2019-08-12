year = int(input("서기 몇 년 ? "))

# 윤년 판정
is_leap = (year % 400 == 0)or((year % 100 != 0)and(year % 4 == 0))

# 결과 표시
if is_leap:
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")

