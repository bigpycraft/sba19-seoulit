customer = {
    "name"    : "김진수",
    'gender'  : '남자',
    "email"   : "bigpycraft@gmail.com",
    "company" : "빅파이크래프트",
    "address" : "서울시 중구 청파로"
}

print(customer.keys())
print(customer.values())
print(customer.items())

for key, value in customer.items():
    print('%s\t : %s' %(key, value))



