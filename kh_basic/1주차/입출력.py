# 표준 입출력 : 콘솔 입출력을 의미한다.
# [] 대괄호: 다른 언어에서는 배열에 쓰인다. 하지만 Python에서는 list를 표시할 때 사용
# {} 증괄호 : 딕셔너리 표시
# () 소괄호 : 함수의 인수, 튜플을 표시할 때 쓴다.

# print() : 화면 출력을 위한 함수
print(36)
print("문자열")
print([1, 2, 3]) # 리스트 출력
print("파"+"이"+"썬")
print("파","이","썬") # ,(콤마) = 구분자 (separator; 기본 값은 공백)
print("파""이""썬")

# 이스케이프 문자 : 출력 구간의 흐름을 제어하기 위해서 사용.
# \n (줄바꿈), \t (탭을 의미), \b  (백스페이스), \r (커서를 맨 앞으로 돌림)
# print("\n\n", sep=" ", end="\n")
# print("\n") #이 경우 2줄을 바꾼다.
#
# print("Banana\b")
# print("Banana\rApple")
# print("Banana", "Apple", "Mango", sep="$")
# year = 2024
# month = 9
# day = 10
# print(year, month, day, sep="-")
#
#
# import time
# for i in range(1, 101):
#     time.sleep(1)
#     print(f"\r{i}%", end="")

# 출력 스타일 정리
name = "invoker"
age = 12
gender = "male"
job = "dev"
addr = "Arcane river"

# 서식 지정지 스타일 (C 언어 방법)
print("============= 서식 지정지 스타일 =============")
print("이름 : %s 성별 : %s"%(name, gender))
print("나이 : %d"%age)
print("주소 : %s"%addr)

# 파이썬 old 스타일
print("============= 파이썬 OLD 스타일 =============")
print("이름 : {} 성별 : {}".format(name, gender))
print("주소 : {}".format(addr))

# 파이썬 현재 스타일
print("============= 파이썬 현재 스타일 =============")
print(f"이름 : {name} 성별 : {gender}")
print(f"주소 : {addr}")

# 문자열 연결 연산자 사용 방식
print("이름 : " + name)
print("나이 : " + str(age)) # age는 문자열이 아니라서 에러가 난다!!! str을 추가해줘서 문자열로 변환해버려야 된다.

# 정렬; > 우측 정렬; < 좌측 정렬; ^ 가운데 정렬
num1 = 10
num2 = 100
num3 = 1000
num4 = 10000
num5 = 3.1459294584450

print(f"|{num1:^8}|")
print(f"|{num2:^8}|")
print(f"|{num3:>8}|")
print(f"|{num4:<8}|")
print(f"|{num5:.2f}|") # 3번째 자리에서 반올림해서 2번째 자리까지 표기. 3.15가 나온다.