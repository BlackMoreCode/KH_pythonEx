# 2개의 문자열을 포인터 변수 s 와 k에, 양의 정수를 정수형 변수
# n에 각기 전달 받아 s 문자열의 뒤 부분에 n개 문자를 k 문자열 앞에 끼어 넣는 코드 작성
# 예) s: seoul
#     k: korea
#     n: 2
#     result: ulkorea

s = str(input())
k = str(input())
n = int(input())

# s = "random"
# k = "string"
# n = 2

result = s[-n:] + k
print(result)