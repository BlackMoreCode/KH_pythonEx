# 프로그램에서 값 연산시 사용
# 산술 연산자 : +, -, *, /, //(몫), %(나머지 연산자), **(제곱 연산자)

i = 10
j = 3

print(i + j)
print(i - j)
print(i * j)
print(i / j)
print(i // j) # 몫
print(i % j)  # 나머지; 알고리즘 단골 주제
print(i ** j) # 10^3

TAX_RATE = 0.25 # 세율
income = input("당신의 수입은 얼마? : ")
# print(f"내야할 세금은 {float(income * TAX_RATE)}")

# 대입 연산자 : 값을 변수에 대입
# 대입 연산자의 종류: =. +=, -=, *=, /=, %=
num1 = 10
num1 += 2 # num1 = num1 + 2
print(num1) # 12
num1 -= 10
print(num1) # 2

num1 *= 2
print(num1) # 4

#비교 연산자 : 값을 비교해서 boolean 값을 반환
# == 같다, > 왼쪽이 크다, >= 왼쪽이 크거나 같다, </<=,
print(10 > 4)
a = 10
b = 20
print(a > b) # false
print(a < b) # true
print (a == b) # false
print (a >= b) # false
print(a <= b) # true

# 관계 연산자 : 연산자 (&&), or (||), not (1)  괄호 안은 자바/자바스크립트의 경우 쓰는 표현. 파이썬은 그냥 영 단어 그대로 쓴다.
# and(&&) 둘 다 참이여야한다 / or(||) 둘 중 하나만 참이면 된다

x = 10
y = 20
z = 30

rst1 = (x > 0) and (x > y) # false
rst2 = (x > 0) or (x > y) # true
rst3 = not((x > 0)) or (x > y) # false
print(rst1, rst2, rst3)

# 3항 연산자 : 항 3개인 연산자
age = int(input("나이를 입력하세요 : "))
is_adult = age > 19 and "성인" or "미성년자"
print(f"당신은 {is_adult} 입니다")


# - 연도가 4로 나누어 떨어 진다.
# - 100으로 나누어 떨어지면 연도는 윤년이 아니다.
# - 400으로 나누어 떨어지면 윤년이다.


year = int(input("년도를 입력 하세요 : "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) :
    print(f"{year}는/은 윤년 입니다.")
else :
    print(f"{year}는/은 윤년이 아닙니다.")