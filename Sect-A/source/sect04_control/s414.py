# if - else 문 예시
signal_color = input('색을 영문으로 나타내어 보세요.')
if signal_color == 'blue':
    print('신호등은 파란색 입니다. 건너가 주세요.')
else:
    print('신호등은 빨간색 입니다. 기다려 주세요.')


# if - elif  -else 문 예시
signal_color = input('색을 영문으로 나타내어 보세요. (blue/red) ')
if signal_color == 'blue':
    print('신호등은 파란색 입니다. 건너가 주세요.')
elif signal_color == 'red':
    print('신호등은 빨간색 입니다, 기다려 주세요.')
else:
    print('잘못된 색입니다')


# nested if 문 예시
signal_color = input('색을 영문으로 나타내어 보세요.')
if signal_color == 'blue':
    print('신호등은 파란색 입니다. 건너가 주세요.')
    is_pass = input('건널 준비가 되셨나요? (yes/no) ')
    if is_pass == 'yes':
        print('네, 건너겠습니다.')
    else:
        print('다음 번에 건너겠습니다.')
elif signal_color == 'red':
    print('신호등은 빨간색 입니다, 기다려 주세요.')
else:
    print('잘못된 색입니다')

