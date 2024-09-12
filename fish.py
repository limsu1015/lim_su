"""

"""
# 붕어빵 재고 데이터 생성
stock = {
    "팥붕어빵" : 10, 
    "슈크림붕어빵" : 8, 
    "초코붕어빵" : 5
}

#len(stock) : 함수  stock.items()
for bread, quantity in stock.items():
    print(f'{bread} : {quantity}')

# 1. 한번에 맛과 개수를 받는거
# order = {}
# bread_kind, bread_count = input("주문 할 붕어빵의 종류와 갯수를 입력해 주세요").split()
# order[bread_kind] = bread_count + "개"
# print(f'주문내역: {order}')
# 2. map함수를 이용해서 bead_count 코드를 개선
# bread_count = map(int, input('주문 할 갯수를 입력해주세요'))
order = {}


bread_kind = input("주문할 붕어빵 종류를 입력하세요 (팥붕어빵, 슈크림붕어빵, 초코붕어빵)")
bread_count = int(input("주문 할 갯수를 입력해주세요"))

order[bread_kind] = bread_count

print(f'주문내역: {order}')


if stock[bread_kind] >= bread_count:
    stock[bread_kind] -= bread_count
    print(f'{bread_kind}: {bread_count}개를 판매히였습니다')
else:
    result = bread_count - stock[bread_kind]
    print(f"{bread_kind}재고가 {result}개 부족합니다")
    


#print(stock)