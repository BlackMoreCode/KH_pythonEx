# 재귀함수 (recursive function): 함수내에서 자기 자신을 호출하는 구조
# 길찾기 등의 알고리즘에서 많이 사용, 효율적인 정렬 알고리즘에서도 사용 된다.

def for_sum(a):
    s = 0
    for i in range(1, a + 1): # 1 부터 a 까지의 합을 구함
        s += i
    return s

num = int(input("정수 입력 : "))
print(for_sum(num))


def while_sum(n):
    s = 0
    while n:
        s += n
        n -= 1
    return s

def while2_sum(n):
    sum = 0
    while True:
        sum += n
        n -= 1
        if n == 0: break
    return sum

# 등차 수열
def gaus_sum(a):
    return int(a * (a+1) / 2)

# 재귀 호출
def recu_sum(a):
    if a == 1: return 1
    else: return a + recu_sum(a-1)

a = int(input("정수를 입력 하세요 : "))
print(while_sum(a))