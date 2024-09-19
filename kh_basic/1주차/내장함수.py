# # 별도로 import를 하지 않고도 사용 할 수 있도록 내장되어 있는 함수
#
# # max() => 매개변수로 전달된 값중 제일 큰 값을 반환
# print(max(32, 45, 67, 12, 45))
# score = list(map(int, input("정수 입력 : ").split())) # list 형으로 정수 값 반환
# print((max(score)))
# print(max([1, 2, 3, 4 ,5 ,6 ,7, 8]))
#
# # min() => 매개변수로 전달된 값중 제일 작은 값을 반환
# print(min(32, 45, 67, 12, 45))
# score = list(map(int, input("정수 입력 : ").split())) # list 형으로 정수 값 반환
# print((min(score)))
# print(min([1, 2, 3, 4 ,5 ,6 ,7, 8]))
#
# # sum = 매개변수로 전달된 연속된 값의 합을 반환
# # 시퀀스 자료형의 값을 모두 더한다.
# print(sum([1, 2, 3, 4, 5, 6]))
# print(sum([1, 2, 3, 4, 5, 6]) / 6)
#
# # 몫과 나머지를 반환, 튜플 형태로 반환 (unpacking)
# print(divmod(sum([1, 2, 3, 4, 5]), 5))
#
# # 정렬 => sorted()
# my_list = [1, 55, 77, 99 , 234, 12, 555]
# print(sorted(my_list)) # sorted 함수의 기본 옵션은 오름차순이다.
# print(sorted(my_list, reverse=True)) # 내림 차순 (반전 옵션을 이용)
# print(len(my_list)) # 요소의 개수(길이)

# 실습
n = list(map(int, input("정수 입력 : ").split()))

# 입력 받은 값 중 최대 값
print(f"최대 값은 : {max(n)} 입니다.")

# 입력 받은 값 중 최소 값
print(f"최소 값은: {min(n)} 입니다.")

# 총점
print(f"총점은 {sum(n)} 입니다.")

# 평균
print(f"평균은 {sum(n) / len(n)} 입니다.")

# 몫 + 나머지
print(f"몫과 나머지는 {divmod(sum(n), len(n))} 입니다")