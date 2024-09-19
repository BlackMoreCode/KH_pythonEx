# 주석은 인터프리터가 번역 안하는 영역.
print("파이썬 스타트.") # 주석 처리.
print(100) # 정수 값 출력
print(33.3333) # 실수 값 출력
print(100 + 200) # 연산자 사용
print (100 < 200) # boolean; true/false

# Python 은 값이 대입될 때 데이터 형이 결정된다.
name = "사육사"
print(name)

"""
식별자 생성 규칙
    * 키워드 (reserved python keywords)사용 금지
    * 특수 문자는 _ (언더 바; under bar) 만 사용 가능
    * 숫자는 사용 가능, 하지만 맨 앞에 올 수는 없다!
    * snake_case : 스네이크 표기법 사용; 단어와 단어 연결 시 언더 바를 사용한다.
"""

name = "임세호"
email = "sehorim1993@gmail.com"
phone = "010-7497-7599"
addr = "마곡서로 133"

print(f"""
이름 : {name}
이메일 : {email}
전화번호 : {phone}
주소 : {addr}
""")