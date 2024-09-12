# 실습 문제
# 성적 입력 받아서 0 ~ 100 사이가 아니면 성적 잘못 입력 했다고 표기.
# 0~100 사이과, 90 이상이면 A를 출력.
# 80 이상이면 B
# 70 이상이면 C
# 60 이상이면 D
# 나머지는 F

while True:
    score = int(input("성적 입력 : "))
    if 0 <= score <= 100 :
        if score < 60 :
            print("F")
        elif score >= 60 and score < 70:
            print("D")
        elif score >= 70 and score < 80:
            print("C")
        elif score >= 80 and score < 90:
            print("B")
        elif score >= 90 :
            print("A")
        break
    else :
        print("입력 오류! 다시 입력하시오.")



# 세자리 정수를 입력 받아 100의자리, 10자리, 1자리로 나누어 담고, 이중 가장 큰 수를 출력
#몫/나머지 기용해서 변수 할당한다.
#if/else문 값 비교

# num = int(input("세자리수 정수 : "))
#
# num_100 = num // 100
# num_10 = (num % 100) // 10 # ???
# num_1 = num % 10
#
# if num_100 > num_10 :
#     if num_100 > num_1 : print(num_100)
#     else : print(num_1)
# else :
#     if num_10 > num_1 : print(num_10)
#     else : print(num_1)



