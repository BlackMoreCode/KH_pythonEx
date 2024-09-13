# 무작위 수를 공백으로 기준하여 입력 받아 홀수와 짝수로 리스트에 나누어 담아 출력

num = list(map(int, input("정수 입력 : ").split()))

# 방법 1
odd_num = []
even_num = []
for i in num:
    if i % 2 == 0: even_num.append(i)
    else: odd_num.append(i)
print(f"방법 1의 홀수 표기 : {odd_num}")
print(f"방법 1의 짝수 표기 : {even_num}")

# 방법 2 lambda 매개변수 : 표현식
# filter(함수, 리스트) : 결과가 참인 것만 걸러 내줍니다.
odd = list(filter(lambda x: x % 2 == 1, num))
even = list(filter(lambda x: x % 2 == 0, num))
print(f"방법 2의 홀수 표기 : {odd}")
print(f"방법 2의 짝수 표기 : {even}")


