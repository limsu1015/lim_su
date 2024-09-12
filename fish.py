"""

"""
# 붕어빵 재고 데이터 생성
stock = {
    "팥붕어빵" : 10, 
    "슈크림붕어빵" : 8, 
    "초코붕어빵" : 5
}

price = {
    "팥붕어빵" : 1000,
    "슈크림붕어빵" : 1500,
    "초코붕어빵" : 2000
}

sales = {
    "팥붕어빵" : 0,
    "슈크림붕어빵" : 0,
    "초코붕어빵" : 0
}
# 시작 선택창
while True:
    mode = input("원하는 모드를 선택해 주세요 (주문, 관리자, 종료):")
    if mode == "종료":
        break






#주문 기능
    if mode == "주문":
        while True:
            order = {}
            bread_kind = input("주문할 붕어빵 종류를 입력하세요 (팥붕어빵, 슈크림붕어빵, 초코붕어빵) 종료를 원하는 경우 '종료'를 입력해 주세요")
            if bread_kind == "종료":
                break

            bread_count = int(input("주문 할 갯수를 입력해주세요"))

            if stock[bread_kind] >= bread_count:
                stock[bread_kind] -= bread_count
                sales[bread_kind] += bread_count
                print(f'{bread_kind}: {bread_count}개를 판매히였습니다')
            else:
                result = bread_count - stock[bread_kind]
                print(f"{bread_kind}재고가 {result}개 부족합니다")


    
            for bread, quantity in stock.items():
                print(f'{bread} : {quantity}')


#관리자 모드
    if mode == "관리자모드":    
        while True:
            bread_kind = input("추가할 붕어빵 종류를 입력하세요 (팥붕어빵, 슈크림붕어빵, 초코붕어빵) 종료를 원하는 경우 '종료'를 입력해 주세요")
            if bread_kind == "종료":
                break
            bread_count = int(input("주문 할 갯수를 입력해주세요"))

            stock[bread_kind] += bread_count
            print(f'{bread_kind}: {bread_count}개가 추가되어 총 {stock[bread_kind]}개 입나다')

            for bread, quantity in stock.items():
                print(f'{bread} : {quantity}')

#정산
print("영업을 종료 합니다")
total_sales = sum(sales[bread] * price[bread] for bread in sales)
print(f"총매출 : {total_sales}원")