# ## 문제
#
# 상근날드에서 가장 잘 팔리는 메뉴는 세트 메뉴이다. 주문할 때, 자신이 원하는 햄버거와 음료를 하나씩 골라, 세트로 구매하면, 가격의 합계에서 50원을 뺀 가격이 세트 메뉴의 가격이 된다.
#
# 햄버거는 총 3종류 상덕버거, 중덕버거, 하덕버거가 있고, 음료는 콜라와 사이다 두 종류가 있다.
#
# 햄버거와 음료의 가격이 주어졌을 때, 가장 싼 세트 메뉴의 가격을 출력하는 프로그램을 작성하시오.
#
# ## 입력
#
# 입력은 총 다섯 줄이다.
# 첫째 줄에는 상덕버거, 둘째 줄에는 중덕버거, 셋째 줄에는 하덕버거의 가격이 주어진다. 넷째 줄에는 콜라의 가격, 다섯째 줄에는 사이다의 가격이 주어진다.
# 모든 가격은 100원 이상, 2000원 이하이다.
#
# ## 출력
#
# 첫째 줄에 가장 싼 세트 메뉴의 가격을 출력한다.
# 햄버거 3개 / 음료 2개 옵션 존재' 출력해야할 것은 세트 메뉴 구성중 햄버거+음료 중 제일 싼거 고른 뒤 - 50원.
# 예를 들어 입력된 가격이 1000 1500 2000 500 600
# 이 경우 우리는 1500 - 50 = 1450원을 출력할 수 있어야한다.

# 첫 시도의 경우
num = list(map(int, input("정수 입력 : ").split()))

burger_price = []
burger_price.append(num[0])
burger_price.append(num[1])
burger_price.append(num[2])

min_bp = min(burger_price)

drink_price = []
drink_price.append(num[3])
drink_price.append(num[4])

min_dp = min(drink_price)

min_set = min_bp + min_dp - 50
print(min_set)

# 2번째 시도 파이썬 특화
min_burger = min(num[:3])
min_drink = min(num[3:5])
print(f"세트 가격 : {min_burger + min_drink - 50}")

# 3번째 방법; 2번의 파이썬 문법은 인덱스 슬라이싱이 기억 안날 경우? C 나 JAVA의 경우는 이렇게 할듯?
min_burgerr = num[0] # 기준값 정하기
min_drinkk = num[3]

for i in range(len(num)):
    if i < 3 and min_burgerr > num[i]:
        min_burgerr = num[i]
    if i > 2 and min_drinkk > num[i]:
        min_drinkk = num[i]

print(f"세트 가격 : {min_burgerr + min_drinkk - 50}")