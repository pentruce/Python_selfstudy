# 키오스크 파이썬 - 폴리버거
# 변수선언

menu = 0  # 주문할 메뉴의  번호
number = 0  # 메뉴의 개수
price = 0  # 메뉴의 가격
total = 0  # 구매한 메뉴의 총합계

print("=" * 40)  # 구분선 출력
print("\n안녕하십니까 폴리버거입니다.\n\n어떤 메뉴를 선택하시겠습니까?\n")
print("=" * 40)  # 구분선 출력

# 반복문 while 메인코드

while True:
    main = input("\n\n버거 = [q], 음료 = [w], 사이드메뉴 = [e]\n\n선택 : ")
    if main == 'q':
        print()
        print()
        print("-" * 15, "버거선택", "-" * 15)
        menu = int(input("\n[1] 통새우 버거 : 가격 4000원\n[2] 폴리 버거 : 가격 6000원\n[3] 치즈 버거 : 가격 5000원\n---: "))

    if main == 'w':
        print()
        print("-" * 15, "음료 선택", "-" * 15)
        menu = int(input("\n[4] 콜라 : 가격 1000원\n[5] 제로 콜라 : 가격 2000원\n[6] 사이다 : 가격 2000원\n[7] 탄산수 : 1500원\n---: "))

    if main == 'e':
        print()
        print("-" * 15, "음료 선택", "-" * 15)
        menu = int(input("\n[8] 해시 브라운 : 가격 3000원\n[9] 30cm 치즈스틱 : 가격 2000원\n[10] 양념 감자 : 1500원\n---: "))

        # 1보다 작거나 10보다 큰 수 입력시 오류발생 문구
    if menu < 1 or menu > 10:
        print("\n<ERROR!>다시 입력해주세요!\n")

    if menu == 1:
        price = 4000
    elif menu == 2:
        price = 6000
    elif menu == 3:
        price = 5000
    elif menu == 4:
        price = 1000
    elif menu == 5:
        price = 2000
    elif menu == 6:
        price = 2000
    elif menu == 7:
        price = 1500
    elif menu == 8:
        price = 3000
    elif menu == 9:
        price = 2000
    else:
        price = 1500

    number = int(input("수량 : "))
    total = total + (number * price)
    print()
    print("합계 : ", total, "원 입니다.")


    if main == 'x':
        print("\n카드 투입구에 카드를 넣어주세요.\n")
        print("-" * 40)
        print()
        print("-" * 40)
        print()

    card = input("\n카드를 넣었으면 Z를 눌러주세요. \n----: ")
    if card == 'z':
            print("\n결제 완료 | 감사합니다! 또 오세요~*^^*!!", total, "원\n")
            break;
    else:
        print("\n다시 시도해주세요.\n")
        continue