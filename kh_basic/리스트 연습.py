# 리스트 : 연속적으로 저장되는 형태의 자료형
# 배열과 다르게 크기 지정이 필요 없음
# 읽고 쓰기 가능 = 뮤터블(mutable)
# 리스트 내 원소들이 같은 자료형일 필요는 없음
# 대괄호로 표시

number = [1, 2, 3, 4 ,5]
fruits = ["apple", "banana", "orange"]
mixed = [1, 'apple', True, 3.14, ["Seoul, Korea"], ["Joestar", "DIO", "Pucci"]]

print(number)
print(fruits[1])
print(f"죠죠 시리즈 : {mixed[5]}")
print(f"WRRRRRRRRY : {mixed[5][1]}")
print(f"HINT : {mixed[5][1][0]}") # 문자열은 그 자체로 배열로 취급된다, 하나하나가 개별적인 요소라서, 인덱스로 뽑을 수 있다!

print(f"SONO CHI NO SADAME : {mixed[5][:2]}")

print(f"{mixed[1:5]}") # 인덱스 1 부터 4까지 표기

# 리스트 연산자 : +, *
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3] ; 문자열 3번 반복. 연산자 오버로딩.

# 리스트 요소 추가하기 : append(), insert()
# append() : 리스트의 마지막에 값을 추가
# insert(인덱스, 값) : 해당 인덱스 위치에 값을 추가

alpha = [1, 2, 3]
alpha.append(4)
print(alpha)

alpha.insert(1, 100)
print(alpha)

# 리스트 제거: pop, remove, clear
# pop() : 인덱스를 넣지 않을 시, 마지막 인덱스를 반환하고 값을 삭제.
# 인덱스를 넣으면 해당 인덱스의 값을 삭제하고 보여줌
print(alpha.pop())
print(alpha.pop(1))
print(alpha)
# remove() :
# clear() :

# remove() : 해당하는 값을 지움; 값이 여러개라면 인덱스가 낮은 것을 지운다
alpha.remove(3)
print(alpha)

del alpha[0] # 인덱스로 값을 제거. 이 경우 0번째 인덱스의 값을 제거했다
print(alpha)

# clear : 리스트 내의 모든 내용을 삭제하고 빈 리스트만을 남김.
alpha.clear()
print(alpha)


# 중복 제거하기
list_redundancy = ["A", "B", "C", "D", "A", "D"]
list_new = []
for e in list_redundancy:
    if e not in list_new:
        list_new.append(e)
print(list_new)

# 리스트 순회
names = ["Joestar", "DIO", "Pucci", "Jotaro", "Polnareff", "Kakyoin"]
for name in names:
    print(f"죠죠의 기묘한 모험 출연인물: {name}", end=" ")
print()

for i in range(len(names)):
    print(f"죠죠의 기묘헌 모험 출현인물: {names[i]}", end=" ")
print()