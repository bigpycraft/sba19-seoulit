#while 문 예시

sigmal_color = ''

while sigmal_color != 'blue' and sigmal_color != 'red':
    sigmal_color = input('색을 영문으로 입력하세요 (blue/red) : ')

    if sigmal_color == 'blue':
        print('신호등은 파란색 입니다. 길을 건너세요!!')
    elif sigmal_color == 'red':
        print('신호등은 빨간색 입니다. 기다리세요.')
    else:
        print('잘못된 색입니다. 다시 입력해 주세요!!')

print('프로그램을 종료합니다.')

