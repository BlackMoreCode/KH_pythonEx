# 2번째 수 찾기
# 입력: 1 2 3 4 5 6 7 8 3 4 5 6 7 8
# 찾아야하는 숫자: 3
# 해당 수의 위치를 반환 : 인덱스가 아님; 9번째 임.
# 없을 시 -1 반환


def second_num(ls, target):
    counter = 0 # 카운터 값 0으로 초기 값 할당
    for i in range(len(ls)):
        if ls[i] == target:
            if counter > 0: return i + 1
            else: counter += 1
    return -1 # 없을시 -1 반환

# 정수 값에 대한 리스트 입력 생성
ls = list(map(int, input("정수를 입력").split()))

# 찾을 수 입력 받기
target = int(input("찾아야하는 숫자"))

#결과 출력
print(f"결과는: {second_num(ls, target)}")