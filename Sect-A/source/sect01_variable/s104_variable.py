coffee1_name = '카페라떼';  coffee1_val = 4000;
coffee2_name = '카푸치노';  coffee2_val = 4500;
coffee3_name = '마끼야또';  coffee3_val = 5000;

# Case 1
# print('손님, ' + coffee1_name + coffee2_name + coffee3_name + '를 주문하셨습니다.')
# print('가격은 ' + coffee1_val + coffee2_val + coffee3_val + '원 입니다.')

# Case 2
# print('손님, ' + coffee1_name + coffee2_name + coffee3_name + '를 주문하셨습니다.')
# print('가격은 ' + str(coffee1_val + coffee2_val + coffee3_val) + '원 입니다.')

# Case 3
coffee_val = coffee1_val + coffee2_val + coffee3_val
print('손님, \n%s, %s, %s를 주문하셨습니다.' % (coffee1_name, coffee2_name, coffee3_name))
print('가격은 %d원 입니다.' % coffee_val)
