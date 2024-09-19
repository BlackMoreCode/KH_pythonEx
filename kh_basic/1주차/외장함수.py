# 외장함수는 import 해서 사용하는 함수. 기본적으로 python 에서 제공하는 것
# 랜덤 함수: 지정한 범위 내에서 임의의 숫자를 만들어 내는 것
import random

for i in range(30):
    rand = random.randrange(0, 10) # 0 에서 10 "미만" 임의의 값을 생성
    print(rand, end=" ")
print()

# 중복되지 않는 로또 번호 생성 : 1 ~ 45 사이의 임의의 수 6개
# 리스트 사용하고, 리스트 내에 임의로 생성한 번호가 있으면, 추가하면 안된다.

# for문 이용시
ls = []
for i in range(6):
    rand_num = random.randrange(1, 46)
    if rand_num not in ls:
        ls.append(rand_num)
print(ls)

# while문 이용시
ls2 = []
while len(ls2) <= 6:
    rand_num2 = random.randrange(1, 46)
    if rand_num2 not in ls2:
        ls2.append(rand_num2)
print(ls2)

# set() 집합을 이용해서 중복을 방지. 집합은 중복을 허용하지 않는다.
ls3 = set()
while len(ls3) <= 6:
    rand_num3 = random.randrange(1, 46)
    ls3.add(rand_num3)
print(ls3)