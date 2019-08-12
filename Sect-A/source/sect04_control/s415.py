# BMI 판정 프로그램
weight = float(input("체중(kg)은 ? "))
height = float(input("키(cm)는 ? "))

# BMI 계산
height = height / 100  # m 으로 고친다
bmi = weight / (height * height)

# BMI 값에 따라 결과로 분기 --- (*1)
result = ""
if bmi < 18.5:
    result = "마름"
if (18.5 <= bmi) and (bmi < 25):
    result = "보통"
if (25 <= bmi) and (bmi < 30):
    result = "가벼운 비만"
if bmi >= 30:
    result = "심한 비만"

# 결과 표시
print("BMI :", bmi)
print("판정:", result)
