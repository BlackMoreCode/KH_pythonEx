# 문자열이란? 문자로 이루어진 데이터의 집합

# 인덱싱: 시퀀스 (리스트, 튜플, 문자열, input) 자료형에서 특정 위치의 요소를 선택하는 작업
# 인덱싱은 0부터 시작
# 슬라이싱: 시퀀스 자료형에서 일부 데이터 추출

# reg_num = input ("주민등록번호 입력 : ")  # 991120-1234567
#
# gender = reg_num[7]
# if gender == "1" or gender == "3" :
#     print("남성입니다.")
# else:
#     print("여성입니다")
#
# #태어난 연도를 구하기 위해서 슬라이싱 하는 테스트
#
# birth_year = reg_num[0:2] # 인덱스 0 부터 인덱스 2 "미만" 까지.
# birth_year = int(birth_year)
# if gender == "1" or gender == "2":
#     birth_year += 1900
# else:
#     birth_year += 2000
#
# print(f"태어난 연도 : {birth_year}")
#
# # 생일 출력 : 0720 => 7월 20일
#
# birth_date = reg_num[2:6]
# # print(birth_date)
# print(f"생일은 : {birth_date[1:2]}월 {birth_date[2:4]}일 입니다.")
#
# # 생년월일
# print("생년월일 : " + reg_num[:6])
# print("뒤 7자리" + reg_num [7:]) # 혹은 [-7:]
#
# Life = "Life is too short, you need Python."
# tmp = Life[0] + Life[1] + Life[2] + Life[3] # 정-말 기본적인 붙여넣기..

# 대소문자 바꾸기 upper(), lower()
a = "Hello Python Program..."
print(a.upper())
print(a.lower())
# 실제 코테 예시 --> 대문자는 소문자로, vice versa

# 문자열 변경 : replace("기존 문자열", "바꿀 문자열")
b = "Hello Python Program..."
n_b = b.replace("Python", "JavaScript")
print(n_b)

# 문자열에 포함된 문자 갯수 세기 및 문자열의 길이 구하기
# 문자 갯수는 문자열 내장함수 : count() 사용. 문자열의 포함된 문자의 갯수를 반환
# 문자 길이는 내장함수 len() 사용; 문자열 길이 반환

c = "Hello Python Program..."
print(c.count("l")) # 해당 문자열에서 "l" 이 몇개 들어갔나 확인. "l" 는 이 내장함수의 매개변수로 전달 되었다.
print(len(c)) # 문자열의 길이를 반환
print(c.__len__()) # 용도는 위와 같으나 이 경우 __len__ 은 c 의 메서드 취급.

# 문자열 찾기 : find(), rfind(), index()
# find() 찾은 문자열의 시작 인덱스 반환, 없을시 -1 반환
# index() 찾은 문자열의 시작 인덱스 반환, 없을시 valueError 발생하고 종료
# rfind() 뒤에서 부터 검색. 찾은 문자열의 인덱스는 앞에서 부터 계산. 없을시 -1 반환?
phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장"))
print(phrase.rfind("가장"))
print(phrase.index("포기"))

print(phrase.find("사자소생"))
# print(phrase.index("사자소생"))

new_phrase = phrase.replace("가장", "나에게")
print(new_phrase)

# 문자열 연산자 : +, *
print("태양고" + "나희도")
print("!"*10)
list = [0] * 10
print(list)

#문자열 양옆의 공백제거 : strip()
d = """
    안녕하세요. 
    문자열의 공백을 제거 하겠습니다.
    네네네네넨네...      
"""

print(d.strip())