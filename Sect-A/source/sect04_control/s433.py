# for Ex1
# bts_members = ['RM', 'SUGAR', 'JIN', 'J-HOPE', 'JIMIN', 'V', 'JeongKook']
bts_members = ['RM', '슈가', '진', '제이홉', '지민', '뷔', '정국']
num = 0

print('foe ex1')
for member in bts_members:
    num += 1
    print('멤버%d ====> %s  \t(이름길이:%d)' % (num, member, len(member)))

# for Ex2
size = len(bts_members)
print('-'*50)
print('foe ex2')
for idx in range(size):
    print('멤버%d ====> %s  \t(이름길이:%d)' % (idx+1, bts_members[idx], len(bts_members[idx])))

