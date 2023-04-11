from datetime import datetime

now = datetime.now()                  # 맥런치 시간 위해
time = 60 * now.hour + now.minute          # (지금 시간 * 60) + 지금 분  ex) 12시 30분 기준 => (12*60)+30

str1 = ''       # 서비스 안내 입력받을 공백

str2 = ''       # 서비스 안내 입력받을 공백 2

menuml = {'빅맥세트':5200,'상하이버거세트':5200,'1955버거세트':6200,'베이컨토마토디럭스세트':6000}
menubu = {'빅맥':4900,'맥스파이시상하이버거':4900,'1955버거':6000,'베이컨토마토디럭스버거':5800,'맥크리스피디럭스':6700,
          '맥크리스피클래식':5900,'맥치킨모짜렐라':5000,'맥치킨':3500,'더블불고기버거':4500,'에그불고기버거':3500,
          '더블필레오피쉬':5200,'필레오피쉬':3700,'슈슈버거':4700,'슈비버거':5800,'쿼터파운드치즈':5500,'더블쿼터파운드피즈':7400,
          '트리플치즈버거':5800,'더블치즈버거':4500,'치즈버거':2500,'햄버거':2200}
menudr = {'카페라떼':3000,'아메리카노':2500,'바닐라라떼':3500,'카푸치노':3000,'에스프레소':1700,'우유':1500,'생수':1200,
          '아이스드랍커피':1500,'탄산음료':1500,'쉐이크':2800}
menusd = {'맥너겟':2200,'맥스파이시치킨텐더':2700,'치즈스틱':2500,'상하이치킨스낵랩':2400,'치킨토마토스낵랩':2200,
          '후렌치후라이':1800,'애플파이':1300,'코울슬로':1900}

all_menu = [menuml,menubu,menudr,menusd]  # 모든 메뉴를 한 곳에 모아놓음
side_drink = ['콜라','사이다','에이드']    # 사이드 드링크 메뉴
door = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]      # 와일 문
cnt = 0        # 총합계
all_add = []          # 장바구니
changeMenu = False     # 메뉴변경을 위한 메뉴

while 1 in door :          # 첫번째 문
    door = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('-' * 25)
    print('1. 매장  2. 포장')
    print('-' * 25)

    c = input('>매장 or 포장 : ')

    if c == '매장' or c == '1' :            # 매장일 경우 변수 저장
        str1 = '매장'
    elif c == '포장' or c == '2' :          # 포장일 경우 변수 저장
        str1 = '포장'
    else :
        print('다시 입력해주세요')
        continue
    while 2 in door :   # 2번째 프레임
        if changeMenu != True :                # 메뉴 변경과 겹치지 않게끔
            door = [1,2,3,4,5,6,7,8,9,10]
            print('-' * 25)
            print('1. 이전  2. 카테고리  3.주문내역  4.완료')
            print('-' * 25)

            f_1 = int(input('>원하는 번호 입력 : '))

        if f_1 == 1 :      # 만약 f_1이 1이라면 이 전 단계로 돌려보낸다
           break
        elif f_1 == 2 :        # 만약 f_1이 2라면 카테고리란으로 넘어간다
            while 3 in door :         # 메뉴 안에서 반복을 위한 3번째 프레임
                door = [1,2,3,4,5,6,7,8,9,10]
                M = int(input('0.맥런치  1.버거  2.음료  3.사이드  4.이전 : '))
                if M == 4 :         # 이전단계로 돌아간다
                    break
                if 630 <= time <= 840 :      # 10시30분부터 2시까지 작동되게 설정했습니다.
                    w1 = list(all_menu[:][M])         # 모든 메뉴에서 선택한 메뉴의 리스트만 가져오게 설정했습니다.
                    print(w1)
                    select2 = input('>먹을 메뉴 선택 : ')
                    if select2 in w1 :                              # 먹을 메뉴를 골라서 안에 있다면 장바구니 all_add에
                        menu_price2 = all_menu[:][M][select2]            # 선택한 메뉴와 가격을 담아줍니다.
                        all_add.append([select2, menu_price2])
                        if select2 in menusd or select2 in menudr :     # 선택한 메뉴가 사이드와 드링크에 있으면
                            continue                                        # 다른 프레임으로 넘어가지 않고 앞으로 넘깁니다.
                        if select2 in menubu:             # 선택한 메뉴가 햄버거 종류라면 재료선택을 위해 넘어간다.
                            while 4 in door:          # 다음 프레임
                                door = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                print('-' * 25)
                                print('1.취소  2.단품  3.세트  4.라지세트')
                                print('-' * 25)
                                f_2 = int(input('>원하는 버튼 클릭 : '))
                                if f_2 == 1 :
                                    all_add.pop()          # 취소라면 선택한 메뉴를 삭제하고 이 전 단계로 돌려놓습니다.
                                    break
                                elif f_2 == 2 or f_2 == 3 or f_2 == 4 :
                                    while 5 in door :                  # 다음 프레임
                                        door = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                        if f_2 == 3 :           # 만약 세트라면 메뉴 이름에 세트와 가격을 추가해주는 것인데
                                            for i in all_add :      # 아직 원하는것 만이 아닌 버거 전체로 설정됩니다.
                                                if i[0] in list(menubu) :    # 버거 리스트 안에 선택한 메뉴가 있다면
                                                    str2 = '세트'        # 세트 글씨 추가와 함께
                                                    i[0] += str2        # 세트 가격을 추가해줍니다.
                                                    i[1] += 1700
                                            print(all_add)
                                        elif f_2 == 4 :           # 이 역시 라지세트 라면 메뉴 이름에 세트와 가격을 추가해주는 것인데
                                            for i in all_add :      # 아직 원하는것 만이 아닌 버거 전체로 설정됩니다.
                                                if i[0] in list(menubu) : # 버거 리스트 안에 선택한 메뉴가 있다면
                                                    i[0] += '라지'        # 라지라는 글자 추가와 함께
                                                    i[1] += 2400          # 라지 값 2400원을 추가해줍니다
                                                    print(all_add)
                                                while 6 in door:                  # 다음 프레임
                                                    door = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                                    print('-' * 25)
                                                    print('1.이전  2. 버거재료  3.사이드재료  4.음료  5.완료')
                                                    print('-' * 25)
                                                    f_3 = int(input('>원하는 버튼 클릭 : '))
                                                    if f_3 == 1:      # 세트메뉴 선택 시 세트와 가격을 이전으로 돌려놓습니다.
                                                        for i in all_add:     # 하지만 이 역시 전체적으로 실행돼 미완성입니다.
                                                            if '세트' in i[0]: # 만약 세트라는 str이 i[0]에 있다면
                                                                c = i[0].replace('세트', '')      #세트라는 글씨를 지우고
                                                                i[0] = c                       # i[0]에 대입하고
                                                                i[1] -= 1700                   # 가격을 지웁니다.
                                                            elif '라지' in i[0]:       # 세트메뉴 선택 시 세트와 가격을 이전으로 돌려놓습니다.
                                                                d = i[0].replace('라지', '')      # 하지만 이 역시 전체적으로 실행돼 미완성입니다.
                                                                i[0] = d                    #라지라는 글씨를 지우고 i[0]에 대입 후
                                                                i[1] -= 2400               # 라지 값을 지웁니다.
                                                        print(all_add)
                                                        break
                                                    elif f_3 == 2:               # 버거재료 선택구성
                                                        print('-' * 25)
                                                        burger1 = input('> 1. 기본구성으로 하시겠습니까?[O/X] : ') # 구성 묻고
                                                        print('-' * 25)
                                                        if burger1 == 'x' or burger1 == 'X':      # 기본구성으로 안하겠다고 하면 아래 출력
                                                            burger2 = input('> 2. 야채1 변경??[O/X] : ')
                                                            burger3 = input('> 3. 야채2 변경??[O/X] : ')
                                                            burger4 = input('> 4. 소스 변경??[O/X] : ')
                                                            burger5 = input('> 5. 패티 변경??[O/X] : ')
                                                            burger6 = input('> 6. 취소?[O/X] : ')
                                                            if burger6 == 'O' or burger6 == 'o':    # 취소시 이 전 단계로 돌아가기
                                                                continue
                                                            burger7 = input('> 7. 완료?[O] : ')   # 완료 시 넘어가기
                                                            if burger7 == 'O':
                                                                continue
                                                        else:
                                                            print('기본구성으로 선택되어 이전 화면으로 돌아갑니다.')
                                                            continue
                                                    elif f_3 == 3:              # 사이드 (감튀 설정)
                                                        print('세트 선택하신 분은 감튀는 따로 선택 안하셔도 됩니다.')
                                                        print('단품은 감자튀김 먼저 선택 하셔야합니다.')
                                                        print('-' * 25)
                                                        side = input('감자튀김 선택[O/X] : ')      # 감자튀김 먹을지 여부 묻기
                                                        print('-' * 25)

                                                        if side == 'x' or side == 'X':      # 안먹는다면 이 전 단계로 돌아가기
                                                            continue
                                                        else:
                                                            for i in all_add:          # 만약 세트나 라지세트면 감튀가 이미 포함되어 있기에 패스
                                                                if '세트' in i[0] or '라지' in i[0]:
                                                                    pass
                                                                elif i[0] in menubu:       # 그게 아니라면 후렌치후라이와 가격 추가 후 내보내기
                                                                    all_add.append(['후렌치후라이', 1800])
                                                                    break
                                                            print(all_add)
                                                        side1 = input('1.소금 포합?[O/X] : ')      # 소금 포함 여부 묻기
                                                        if side1 == 'O' or side1 == 'o':
                                                            print('소금 추가')
                                                        side2 = input('2.취소?[O/X] : ')     # 취소 여부 묻기
                                                        if side2 == 'o' or side2 == 'O':     # 취소 한다면 마지막에 들어온
                                                            all_add.pop()                    # 삭제 후 이 전 단계로 내보내기
                                                            print(all_add)
                                                            continue
                                                        side3 = input('3.완료?[O] : ')       # 완료 시 넘기기
                                                        if side3 == 'o' or side3 == 'O':
                                                            continue
                                                    elif f_3 == 4:      # 음료 구성 선택
                                                        while True:
                                                            print('단품은 음료 추가 선택 하셔야합니다.')
                                                            print()
                                                            print('세트는 기본적으로 콜라가 포함되어 있습니다.')
                                                            print('-' * 25)
                                                            drink = int(input('1.선택안함  2.콜라  3.사이다  4.에이드  5.취소  6.완료 : '))  # 선택할 음료 받고
                                                            print('-' * 25)
                                                            if drink == 1:   # 선택안함시 내보내기
                                                                break
                                                            for i in all_add:     # 세트나 라지가 메뉴에 있을경우 가격 추가는 제외
                                                                print(i)
                                                                if '세트' in i[0] or '라지' in i[0]:
                                                                    if drink == 2:
                                                                        print('기본 선택구성입니다.')
                                                                    elif drink == 3:
                                                                        print('사이다로 변경합니다')
                                                                    elif drink == 4:
                                                                        print('에이드로 변경합니다')
                                                                elif '세트' not in i[0]:        # 메뉴에 세트가 없다면 가격 추가
                                                                    if drink == 2:
                                                                        exchange = int(input('> 1. 변경 or 2. 추가 : '))
                                                                        if exchange == 1:          # 음료 변경
                                                                            if i[0] not in side_drink:
                                                                                print('메뉴가 선택되지 않아 변경이 불가합니다.')
                                                                        if exchange == 2:        # 추가일 시 음료 추가
                                                                            all_add.append(['콜라', 1500])
                                                                        break
                                                                    elif drink == 3:            # 사이다를 골랐을 경우 단품일때
                                                                        exchange = int(input('> 1. 변경 or 2. 추가 : '))
                                                                        if exchange == 1:
                                                                            if i[0] not in side_drink:
                                                                                print('메뉴가 선택되지 않아 변경이 불가합니다.')
                                                                        if exchange == 2:
                                                                            all_add.append(['사이다', 1500])
                                                                        break
                                                                    elif drink == 4:          #환타를 골랐을 경우 단품일때
                                                                        exchange = int(input('> 1. 변경 or 2. 추가 : '))
                                                                        if exchange == 1:
                                                                            if i[0] not in side_drink:
                                                                                print('메뉴가 선택되지 않아 변경이 불가합니다.')
                                                                        if exchange == 2:
                                                                            all_add.append(['에이드', 1500])
                                                                        break
                                                            if drink == 5:        # 취소
                                                                break
                                                            if drink == 6:          # 완료
                                                                break

                                                    elif f_3 == 5:    # 2번째 프레임으로 나가기
                                                        del door[5]
                                                        del door[4]
                                                        del door[3]
                                                        del door[2]
                                                        break
                elif M == 0 :          # 맥런치 타임이 아니라면 클릭할 수 없도록 맥런치 선택이 불가능하도록 정했습니다.
                    if time < 630 or time > 840 :
                        print('맥런치 시간이 아닙니다')
                else :                 # 맥런치 타임 외 / 아래 구성은 맥런치타임과 같습니다. 그래서 따로 코드를 적진 않았습니다.
                    w2 = list(all_menu[:][M])
                    print(w2)
                    select1 = input('>먹을 메뉴 선택 : ')
                    if select1 in w2 :
                        menu_price1 = all_menu[:][M][select1]
                        all_add.append([select1, menu_price1])
                        if select1 in menusd or select1 in menudr :
                            continue
                        if select1 in menubu :
                            while 4 in door:
                                door = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                print('-' * 25)
                                print('1.취소  2.단품  3.세트  4.라지세트')
                                print('-' * 25)
                                f_2 = int(input('>원하는 버튼 클릭 : '))
                                if f_2 == 1 :
                                    all_add.pop()
                                    break
                                elif f_2 == 2 or f_2 == 3 or f_2 == 4 :
                                    while 5 in door :
                                        door = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                        if f_2 == 3 :
                                            for i in all_add :
                                                if i[0] in list(menubu) :
                                                    str2 = '세트'
                                                    i[0] += str2
                                                    i[1] += 1700
                                            print(all_add)
                                        elif f_2 == 4 :
                                            for i in all_add :
                                                if i[0] in list(menubu) :
                                                    i[0] += '라지'
                                                    i[1] += 2400
                                            print(all_add)
                                        while 6 in door :
                                            door = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                            print('-' * 25)
                                            print('1.이전  2. 버거재료  3.사이드재료  4.음료  5.완료')
                                            print('-' * 25)
                                            f_3 = int(input('>원하는 버튼 클릭 : '))
                                            if f_3 == 1 :
                                                for i in all_add :
                                                    if '세트' in i[0] :
                                                        c = i[0].replace('세트','')
                                                        i[0] = c
                                                        i[1] -= 1700
                                                    elif '라지' in i[0] :
                                                        d = i[0].replace('라지','')
                                                        i[0] = d
                                                        i[1] -= 2400
                                                print(all_add)
                                                break
                                            elif f_3 == 2 :
                                                print('-' * 25)
                                                burger1 = input('> 1. 기본구성으로 하시겠습니까?[O/X] : ')
                                                print('-' * 25)
                                                if burger1 == 'x' or burger1 == 'X' :
                                                    burger2 = input('> 2. 야채1 변경??[O/X] : ')
                                                    burger3 = input('> 3. 야채2 변경??[O/X] : ')
                                                    burger4 = input('> 4. 소스 변경??[O/X] : ')
                                                    burger5 = input('> 5. 패티 변경??[O/X] : ')
                                                    burger6 = input('> 6. 취소?[O/X] : ')
                                                    if burger6 == 'O' or burger6 == 'o' :
                                                        continue
                                                    burger7 = input('> 7. 완료?[O] : ')
                                                    if burger7 == 'O' :
                                                        continue
                                                else :
                                                    print('기본구성으로 선택되어 이전 화면으로 돌아갑니다.')
                                                    continue
                                            elif f_3 == 3 :
                                                print('세트 선택하신 분은 감튀는 따로 선택 안하셔도 됩니다.')
                                                print('단품은 감자튀김 먼저 선택 하셔야합니다.')
                                                print('-' * 25)
                                                side = input('감자튀김 선택[O/X] : ')
                                                print('-' * 25)

                                                if side == 'x' or side == 'X' :
                                                    continue
                                                else :
                                                    for i in all_add:
                                                        if '세트' in i[0] or '라지' in i[0] :
                                                            pass
                                                        elif i[0] in menubu :
                                                            all_add.append(['후렌치후라이',1800])
                                                            break
                                                    print(all_add)
                                                side1 = input('1.소금 포합?[O/X] : ')
                                                if side1 == 'O' or side1 == 'o' :
                                                    print('소금 추가')
                                                side2 = input('2.취소?[O/X] : ')
                                                if side2 == 'o' or side2 == 'O' :
                                                    all_add.pop()
                                                    print(all_add)
                                                    continue
                                                side3 = input('3.완료?[O] : ')
                                                if side3 == 'o' or side3 == 'O' :
                                                    continue
                                            elif f_3 == 4 :
                                                while True :
                                                    print('단품은 음료 추가 선택 하셔야합니다.')
                                                    print()
                                                    print('세트는 기본적으로 콜라가 포함되어 있습니다.')
                                                    print('-' * 25)
                                                    drink = int(input('1.선택안함  2.콜라  3.사이다  4.에이드  5.취소  6.완료 : '))
                                                    print('-' * 25)
                                                    if drink == 1 :
                                                        break
                                                    for i in all_add :
                                                        print(i)
                                                        if '세트' in i[0] or '라지' in i[0] :
                                                            if drink == 2 :
                                                                print('기본 선택구성입니다.')
                                                            elif drink == 3 :
                                                                print('사이다로 변경합니다')
                                                            elif drink == 4 :
                                                                print('에이드로 변경합니다')
                                                        elif '세트' not in i[0] :
                                                            if drink == 2 :
                                                                exchange = int(input('> 1. 변경 or 2. 추가 : '))
                                                                if exchange == 1 :
                                                                    if i[0] not in side_drink :
                                                                        print('메뉴가 선택되지 않아 변경이 불가합니다.')
                                                                if exchange == 2 :
                                                                    all_add.append(['콜라',1500])
                                                                break
                                                            elif drink == 3 :
                                                                exchange = int(input('> 1. 변경 or 2. 추가 : '))
                                                                if exchange == 1 :
                                                                    if i[0] not in side_drink :
                                                                        print('메뉴가 선택되지 않아 변경이 불가합니다.')
                                                                if exchange == 2 :
                                                                    all_add.append(['사이다',1500])
                                                                break
                                                            elif drink == 4:
                                                                exchange = int(input('> 1. 변경 or 2. 추가 : '))
                                                                if exchange == 1:
                                                                    if i[0] not in side_drink:
                                                                        print('메뉴가 선택되지 않아 변경이 불가합니다.')
                                                                if exchange == 2:
                                                                    all_add.append(['에이드', 1500])
                                                                break
                                                    if drink == 5 :
                                                        break
                                                    if drink == 6 :
                                                        break

                                            elif f_3 == 5 :
                                                del door[5]
                                                del door[4]
                                                del door[3]
                                                del door[2]
                                                break

                                        break
                    else :
                        print('잘못 입력하셨습니다.')
                        continue
        elif f_1 == 3 :        # 주문내역 출력
            print('------[Order List]-------------------------------------------------------------')
            print(all_add)
            print('-------------------------------------------------------------------------------')
            print()
            continue
        elif f_1 == 4 :                  # 리스트에서 완료버튼 클릭 후
            if len(all_add) >= 1 :       # 장바구니가 1개 이상일 경우
                while 7 in door :
                    door = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                    print(f'''{all_add}고객님께서 선택하신 메뉴입니다.''')       # 선택한 메뉴 출력
                    user = int(input('> 1. 변경  2. 확인 : '))
                    if user == 1 :             # 1 변경일 경우 리스트 출력
                        want = int(input('> 1.메뉴변경  2.삭제  3.수량변경  4.취소  5.완료 : '))
                        if want == 1 :            # 메뉴변경을 할 경우
                            print(all_add)       # 장바구니 출력 후
                            deleteMenu = input('변경할 메뉴를 입력하세요 : ') # 변경할 메뉴 선택
                            for item in all_add :      # 그 중 반복문으로 돌리면서
                                if item[0] == deleteMenu :    # 내가 선택한 메뉴와 리스트가 일치하다면
                                    all_add.remove(item)      # 리무브로 값 제거 후
                            changeMenu = True               # 위로 올려보내서 새로운 메뉴 선택
                            break
                        elif want == 2 :             # 삭제 원할 경우
                            print(all_add)          # 장바구니 출력 후
                            deleteMenu = input('삭제할 메뉴를 입력하세요 : ')     # 삭제 할 메뉴 지정
                            for item in all_add:        # 앞에 1번 변경할 때와 방법은 같다
                                if item[0] == deleteMenu :
                                    print(item[0])
                                    all_add.remove(item)
                            print(all_add)
                            continue
                        elif want == 3 :         # 수량 변경
                            print(all_add)      # 장바구니 출력
                            QualityMenu = input('수량 변경할 메뉴를 입력하세요 : ')       # 변경 할 메뉴 지정
                            for item in all_add :
                                if QualityMenu in item[0] :     # 변경 할 메뉴가 장바구니에 있다면
                                    plus = int(input('> 몇 개 추가하시겠습니까? : '))   # n 개 추가
                                    minus = int(input('> 몇 개 빼시겠습니까? : '))     # n 개 삭제
                                    if plus >= 1 :       # 추가가 1과 같거나 크다면
                                        item[1] += item[1] * plus      # 가격에 갯수 곱해주고
                                        item[0] += str(plus+1) + '개'    # n+1개를 더해준다
                                    # if minus >= 1 :       # 뺄 개수가 1과 같거나 크다면
                                    #     item[1] -= item[1] * minus          # 마이너스 가격을 빼주고
                                    #     item[0] += str(minus-1) + '개'       # 역시 해줘야하는데 아직 오류가 난다
                                    #     if item[1] <= 0 :
                                    #         continue
                            print(all_add)
                        elif want == 4 :
                            all_add = []        # 아직 미완성
                            print(all_add)
                            # 메뉴 변경했던것도 돌아와야하고 / 삭제했던것이나 / 수량변경 했던것이 모두 돌아와야한다.
                    if user == 2 :        # 확인을 눌렀을 경우
                        while 8 in door :
                            door = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                            print('-' * 25)
                            print('1. 테이블서비스  2.셀프')
                            print('-' * 25)
                            service = int(input('> 번호를 선택해주세요 : '))
                            if service == 1 :          #1번 선택시 str1에 테이블 서비스 추가
                                str1 += ' / 테이블서비스'
                                print(str1)
                            elif service == 2 :        #2번 선택시 str1에 셀프 서비스 추가
                                str1 += ' / 셀프'
                                print(str1)
                            else :
                                print('다시 입력해주세요')
                            while 9 in door :
                                print('-' * 25)
                                print('1. 취소  2.결제')
                                print('-' * 25)
                                end = int(input('> 번호를 선택해주세요 : '))
                                if end == 1 :  # 여태껏 입력된 정보를 초기화하고 첫 프레임으로 되돌려보낸다
                                    all_add = []        # 장바구니 초기화
                                    del door[8]              # .
                                    del door[7]              # .
                                    del door[6]              # .
                                    del door[5]              # .
                                    del door[4]
                                    del door[3]
                                    del door[2]
                                    del door[1]
                                    break
                                elif end == 2 :        # 종료하고 장바구니와 서비스 상태를 출력해준다
                                    print(all_add)          # 장바구니 출력
                                    for item in all_add :    # 총합계 계산하는 코드
                                        cnt += item[1]
                                    print(str(cnt) + '원')              # 총합계
                                    print(str1)             # 서비스 상태 출력 ( 어디서 먹는지,직접 가져오는지 )
                                    del door[8]
                                    del door[7]
                                    del door[6]
                                    del door[5]
                                    del door[4]
                                    del door[3]
                                    del door[2]
                                    del door[1]
                                    del door[0]
                                    break
