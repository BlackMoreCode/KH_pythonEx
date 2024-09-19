# 사용자에게 콘솔로 입력을 받아 변수에 대입
# input() 함수를 사용
# input() 함수는 문자열로 입력을 받음



# # 정수 타입으로 변수에 값을 대입하기 위해서는 형 변환이 필요하다.
# #이름, 나이, 주소, 직업, 성적(실수 타입;float)를 입력 받아 출력하기
#
# name = input("이름을 입력하세요 : ")
# # print(f"당신의 이름은 {name} 입니다.")
#
# addr = input("주소를 입력하세요 : ")
# # print(f"주소는 {addr} 입니다.")
#
# age = int(input("나이를 입력하세요 : "))
# # print(age + 10)
#
# job = input("직업을 명시해주세요 : ")
# # print(f"직업은 {job} 입니다.")
#
# grade = float(input("성적을 입력해주세요 :"))
# # print(f"성적은 {grade} 입니다.")
#
# print(f"안녕하세요? \"{name}\"님")    # 코드내에서  이스케이프 문자 (\)를 넣고 쌍 따옴표로 강조
# print(f"당신의 주소는 {addr} 이고 직업은 {job} 이고,  나이는 {age} 입니다.")
# print(f"당신의 성적은 {grade:.2f} 입니다")


# 국어 영어 수학 과학 성적을 공백 기준으로 입력 받아 총점을 구하기
# 1번째 방법 ; 동시에 여러개 형 변환을 진행할 시 map 함수를 이용 한다.
# kor, eng, mat, scn = map(int, input("성적 입력 : ").split())
# print(f"총점: {kor + eng + mat + scn}")
# print(f"평균: {(kor + eng + mat + scn) / 4}")

#2번째 방법
# 하드코드 되지 않고 score를 쓰는 만큼 유연하게 계산한다.. 마치 JS에서 쓰던 고차함수 하듯이.
# score = list(map(int, input("성적 입력 : ").split()))
# print(f"총점: {sum(score)}")
# print(f"평균 : {sum(score) / len(score)}") # len = length

# 24시간제 시간을 : 기준으로 입력 받아서 시, 분, 초로 찍는데 12시간제로 변환
hour, min, sec = map(int, input("시:분:초 : ").split(":")) # : 기준으로 쪼갰으니까 split 함수 매개변수에 명시한다

if hour > 12:
    hour -= 12 # hour = hour - 12
    print(f"오후 {hour}시 {min}분 {sec}초")
else:
    print(f"오전 {hour}시 {min}분 {sec}초")

