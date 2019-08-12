# 사전형 생성
bans = { '잎새반':'찬영이',
         '열매반':'예영이',
         '햇살반':'준영이',
         '열매반':'채영이', }

print(type(bans))
print('반의수 : ', len(bans))

# 읽기
print('잎새반 : ', bans['잎새반'])
print('열매반 : ', bans['열매반'])
print('bans 읽기 :', bans)

# 추가
bans['꽃잎반'] = '희영이'
print('bans 추가 :', bans)

# 변경
bans['잎새반'] = '서영이'
print('bans 변경 :', bans)

# 삭제
del bans['햇살반']
print('bans 삭제 :', bans)

