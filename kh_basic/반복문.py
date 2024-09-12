# 조건이 참인 동안 반복 수행
# n = int(input("정수 입력: "))
# sum = 0
# while n:
#     sum += n
#     n -= 1
# print(sum)
#
# for i in range(1, n + 1): # 범위 기반의 for문
#     sum += i
# print(sum)
#
#
# while True: #무한 루프를 방지하기 위하여 탈출 조건이 있어야 한다..
#     age = int(input("나이를 입력 하세요 : "))
#     if 0 < age < 200:
#         print(f"당신의 나이는 {age}살 이군요.")
#         break # 정상적으로 값이 입력 되었으므로 반복문을 벗어 난다.
#     else: print("나이 입력 범위를 벗어 났습니다.")

# for 문: 정해진 범위 만큼을 반복 수행할 때 적합
# for 요소 in 시퀀스 (sequence): 시퀀스 자료에 대한 자동 순회
# for 인덱스 in range(시작 값, 종료 값, 증감 값):

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits: # for..in 반복문
#     print(fruit)
#
# # name = "quaswexexort"
# # for e in name:
# #     print(e, end="-")
#
# for e in input("문자열 입력 :"):
#     print(e, "-")
#
# #for 인덱스 in range (시작값, 종료값, 증감값):
# n = int(input("정수 값 입력  : "))
# sum = 0
# for i in range(n + 1): # 증감 값이 1이면 생략 가능
#     sum += i
# print(sum)

# 양의 정수 n을 입력 받아 n * n 크기의 행렬을 출력하는 프로그램 작성하시오
# 이때 행렬의 값은 1부터 시작하여 왼쪽에서 오른쪽, 위에서 아래 순서대로 채워 넣어라
# 입력 : 4
#  1  2  3  4
#  5  6  7  8
#  9 10 11 12
# 13 14 15 16

# 1. 입력 받은 값으로 살제 출력 범위를 계산해야한다
# 2. 줄바꿈에 대한 처리
# 3. 줄맞춤
#
# n = int(input("정수 값 입력  : "))
#
# for i in range(1, n * n + 1): # +1 안하면 0에서부터 쟨거라 의도한 수보다 1 낮을 것이다.
#     print(f"{i:>4}", end="") # f 스트링 정렬 룰:" < 왼쪽 || > 오른쪽 || ^ 가운데.  숫자는 자릿수를 의미?
#     if i % n == 0: print() # 줄바꿈 처리용. i를 n 으로 나눴을 때 딱 맞아 떨어진다면 줄바꿈이 필요하다


# 2중 for문
# n = int(input("정수 입력 :"))
# for i in range(n): #0 ~ n 미만까지
#     print(f"i={i} ", end="")
#     for j in range (n):
#         print("*", end=" ")
#     print()

# 2중 for문으로 구구단
# for i in range(2, 10): #2~9단의 경우
#     for j in range(1, 10):
#         print(f"{i} X {j} = {i * j}")
#     print("-"*20)

# 제어문 : break, continue
# break: 반복문 탈출용
# continue: 아래의 문장을 수행하지 않고 반복문의 조건식으로 이동 (해달 루틴은 수행한 것으로 간주)
# n = int(input("정수 입력 : "))
# for i in range(n):
#     if i % 2 == 0: continue
#     print(i)

#반복문 반대로 수행
n = int(input("정수 입력 : "))
for i in range(n, 0 - 1, -1): # 시작/최종/증감 값; 0 -1 을 해줘야 0 까지 돈다!
        print(f"인덱스 : {i}")

# for문으로 알파벳 출력
# chr() : 유니코드를 입력 받아서 그 코드에 해당하는 문자를 출력
# ord(): 문자의 유니코드 값을 돌려주는 함수

for i in range(ord("A"),ord("Z")+1): 
    print(chr(i), end=" ") # chr 문자 출력
print()

for i in range(65,91):#A:65 Z:90
	print(chr(i), end=" ")
print()