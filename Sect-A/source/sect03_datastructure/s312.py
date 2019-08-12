# 리스트형 추가/삭제
sistar_members = ['효린', '소유']
print('씨스타 \t:', sistar_members)

sistar_members.append('다솜')
print('append \t:', sistar_members)
sistar_members.insert(1, '보라')
print('insert \t:', sistar_members)

sistar_members.remove('소유')
print('remove \t:', sistar_members)

pickup = sistar_members.pop(0)
print('pop   \t:', sistar_members, end=' ---> ')
print(pickup)
