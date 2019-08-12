# 어떤 유원지의 입장료를 계산하는 프로그램
# 고객 수 입력
children = int(input("어린이 요금(13세 미만)은 몇 명? "))
normal = int(input("보통 요금(13세~64세)은 몇 명? "))
elder = int(input("경로우대요금(65세 이상)은 몇 명? "))

# 집계
total_num = children + normal + elder
children_price = children * 500
normal_price = normal * 1000
elder_price = elder * 700
total_price = children_price + normal_price + elder_price

# 할인 대상인지 확인 ----------- (*1)
if total_num >= 10:
    print("단체 할인됩니다.")
    total_price = total_price * 0.8
else:
    print("단체 할인되지 않습니다.")

# 결과 표시
print("어린이 요금 \t: {0}명x 500 = {1}원".format(children, children_price))
print("보통 요금   \t: {0}명x1000 = {1}원".format(normal, normal_price))
print("경로우대요금\t: {0}명x 700 = {1}원".format(elder, elder_price))
print("합계: {0}人 {1}원".format(total_num, total_price))

