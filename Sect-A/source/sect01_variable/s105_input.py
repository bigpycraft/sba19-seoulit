
def main():
    # Case 1
    name = input('당신의 이름은 무엇입니까? ')
    print(name + '님, 반갑습니다.')

    return


    # Case 2
    order = input('OO카페입니다. \n무엇을 주문하시겠습니까? ')
    count = input('몇 잔을 드릴까요? ')

    print('%s %s잔을 주문하셨습니다. \n잠시만 기다려주세요~^^' % (order, count))

    # Case 3
    price = 4500
    cost  = price * count

    print('%s %s잔을 주문하셨습니다. \n결재하실 금액은 %s원입니다~^^' % (order, count, cost))

    # Case 4
    price = 4500
    cost  = price * int(count)

    print('%s %s잔을 주문하셨습니다. \n결재하실 금액은 %d원입니다~^^' % (order, count, cost))


if __name__ == '__main__':
    main()

print("프로그램 종료")