while input() != 'q':
    try:
        front, back = input("주민등록번호를 입력해주세요(ex. 990101-1234567). 종료하려면 q를 입력하세요. > ").split('-')
        check_id(front,back)

    except:
        print("잘못된 번호입니다. \n올바른 번호를 넣어주세요.")