# 입력 받은 수 미만의 소수의 합 구하기
# 소수란 1과 자기자신으로만 나누어지는 숫자 ~~엔리코 푸치... made-in-heaven~~
# e.g. 입력 : 12 => (2 + 3 + 5 + 7 + 11 = 28)



def prime_func(n): # 소수를 판별하는 함수
    is_prime = True
    for i in range(2, n): # 1과 자기 자신을 제외 --> 즉 소수의 조건을 배제. 즉 여기서 나눠지면 소수가 아니다...!
        if n % i == 0: is_prime = False # 나눠지면 0 이 나오고, 그럼 소수가 아니다.
    if is_prime: return n
    else: return 0

n = int(input("정수 입력 : "))
# is_prime = prime_func(n)
# if is_prime: print("소수")
# else: print("소수가 아니다")

prime_sum = 0 # 합계 값; 0으로 초기 값을 할당
for i in range(2, n):
    prime_sum += prime_func(i)
print(prime_sum)