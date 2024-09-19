# # 함수 = 코드의 틍적 블럭을 하나의 이름으로 묶는 것. 코드의 재사용성 및 가독성 향상
# # 함수는 매개변수를 가질 수 있고, 반환 값을 가질 수 있음
# # 식별자는 스네이크 표기법으로 작성하고, 식별자 뒤에 () 소괄호가 있음.
# # "일반적"으로 매개변수와 함수의 호출하는 인자의 갯수가 일치해야한다.
# # def 키워드를 사용해서 정의. (파이썬의 특징)
#
# # 함수의 반복호출; 매개변수는 존재, 반환값은 없는 함수.
# def name_card(name, addr, phone, position) :
#     print(f"{position} : {name}")
#     print(f"주소 : {addr}")
#     print(f"전화번호 : {phone}")
#     print("-"*30)
#
# # name_card("안유진", "서울시 강남구 역삼동", "010-1234-5678", "리더")
# # name_card("장원영", "서울시 강남구 삼성동", "010-1234-9999", "센터")
# # name_card("가을", "수원시 권선구 권선동", "010-1234-1111", "싱어")
#
# #은행 계좌 개설하기; 반환 값이 있는 함수
# # 계좌 개설
# def open_account(name): #매개변수, 반환값 둘 다 존재하는 함수를 선언
#     print(f"{name}님의 계좌가 개설 되었습니다.")
#     return name
#
#
# def deposit(balance, input):
#     print(f"{input} 입금 되었습니다. 잔액은 {balance + input}입니다.")
#     return balance + input
#
#
# def withdraw(balance, input):
#     if balance >= input:
#         print(f"출금 되었습니다. 잔액은 {balance - input}입니다.")
#         return balance - input
#     else:
#         print(f"출금이 실패 했습니다. 잔액은 {balance}입니다.")
#         return balance
#
#
# balance = 0  # 외부에서 선언된 변수 이지만 인수로 넘겨줘서 결과를 리턴 받음
# name = open_account("정경수")
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
# print(f"{name}의 잔액은 {balance}입니다.")


# # 기본 값 인자: 함수 선언시 매개변수에 대한 기본값을 정의
# # 매개변수에 기본 값이 정의 되어 있는 경우 호출 시 인자 값을 넣지 않으면 기본 값으로 호출
# def profile(name, grade = 2, age = 18, school = "태양고"):
#     print(f"이름 : {name}, 학교 : {school}, 학년 : {grade}, 나이 : {age}")
#
# profile("나희도")
# profile("고유림")
# # profile() #name은 기본 값 인자가 아니기에 반드시 인자 값을 전달해야한다.
# profile("백이진", None, 22)
#
# # 가변 매개 변수: 함수의 매개변수 앞에 *(별표)를 붙이면 인자 값으로 몇개를 전달하든 함수 내에서 튜플로 인식
#
# def profile2(name, age, *lang) :
#     print(f"이름 : {name}, 나이 : {age}", end= " ")
#     for e in lang :
#         print(e, end= " ")
#     print()
#
# profile2("나희도", 18, "Python", "Java", "C", "C++", "React", "Kotlin")
# profile2("조세호", 38, "Python", "JavaScript", )
# profile2("유재석", 48, "Python", "Java", "C", "C++",)
#
#
# # 지역 변수 / 전역 변수
# # 대부분의 언어는 블록 스코프를 기반으로 변수의 생명주기를 관리
# # 파이썬의 경우는 함수 스코프를 기반의 언어. 외부에서 선언한 변수의 값을 함수 내에서 변경하기 위해서는 global 키워드를 사용해야한다.

# knife = 10
# def game(player):
#     global knife
#     knife = knife - player
#     print(f"남아 있는 칼은 {knife} 자루 입니다.")
#
# def game2(player, knife):
#     knife = knife - player
#     print(f"남아 있는 칼은 {knife} 자루 입니다.")
#
#
# in_val = int(input("경기에 참여하는 선수가 몇명 입니까? "))
#
# # game(in_val)
# game2(in_val, knife)


# 키를 입력 받아 표준 체중 구하기
# - 키는 CM 단위로 입력 받습니다.
# - 체중에 대한 출력은 소수점 2자리까지 출력 합니다.(반올림 함수에 대해 사용)

# def std_weight(height, gender):
#     hm = height / 100 # 입력 받은 cm 키를 미터 단위로 변경
#     if gender == "1":
#         return hm * hm * 22
#     else:
#         return hm * hm * 21
#
# height = int(input("키를 입력 : "))
# gender = int(input("성별: [1] 남성 / [2]여성 : "))
# gender_str = "", "남성", "여성"
# weight = round(std_weight(height, gender), 2) # 결과값을 소숫점 3번째 자리에서 반올림해서 2자리를 표시 하는 메서드
# print(f"키 : {height}cm {gender_str[gender]}의 표준 체중은 {weight}kg 입니다.")

# ## 아이패드 구입 하기
#
# - 현재 시간 및 날짜 가져오는 내장 함수 사용
# - 전역 변수 사용
# - 시리얼넘버란? 제품의 고유번호이며 유일한 값
# - `enumerate(iterable, start=0)` : iterable(반복가능한 객체), start(인덱스의 시작값, 기본값은 0)
# - `if sel in map(str, range(1, len(options) + 1)):` `sel`이 유효한 값인지 확인하는 조건문

from datetime import datetime  # 날짜와 시간을 사용하기 위해서
import time  # 시간 관련 기능을 사용하기 위해 import

make_cnt = 0  # 전역변수, 생산 대수를 구하기 위해서

# 공통 선택 함수
def select_option(prompt, options):
    while True:
        print(prompt)
        for idx, option in enumerate(options, start=1):
            print(f"[{idx}] {option}")
        sel = input("선택하세요: ")
        if sel in map(str, range(1, len(options) + 1)):
            return sel

def choice_pad():
    return select_option("<< iPad Pro 구입하기 >>", ("구입하기", "종료하기"))

def select_screen():
    return select_option("디스플레이를 선택 하세요:", ("11인치", "12.9인치"))

def select_color():
    return select_option("컬러를 선택 하세요:", ("스페이스그레이", "실버"))

def select_memory():
    return select_option("용량을 선택 하세요:", ("128GB", "256GB", "512GB", "1TB"))

def select_network():
    return select_option("네트워크를 선택 하세요:", ("Wi-Fi", "Wi-Fi+Cellular"))

def select_name_service():
    sel = select_option("각인 서비스를 선택 하세요:", ("각인 서비스 신청", "신청 안함"))
    if sel == "1":
        return input("이름을 입력하세요: ")
    return "NONE"

def make_ipad(screen, color, memory, network, name):
    global make_cnt
    make_cnt += 1

    # 선택된 옵션에 따른 출력 (튜플 사용)
    screen_options = ("", "11인치", "12.9인치")
    color_options = ("", "스페이스그레이", "실버")
    memory_options = ("", "128GB", "256GB", "512GB", "1TB")
    network_options = ("", "Wi-Fi", "Wi-Fi+Cellular")

    # 시리얼 넘버 생성
    serial_screen = "11" if screen == "1" else "13"
    serial_network = "W" if network == "1" else "C"
    serial_date = datetime.today().strftime("%Y%m%d")
    serial_number = f"iPad{serial_screen}{serial_network}{serial_date}{make_cnt}"

    # iPad 제작 진행 표시 (30초 동안 진행률 표시)
    print("\n아이패드 제작중...")

    for i in range(1, 31):
        print(f"\r제작중... [{i * 100 // 30}%]", end='')  # 진행률 표시
        time.sleep(1)  # 1초 대기

    print("\n\niPad Pro가 출고 되었습니다.")
    print("=" * 34)
    print(f"화면 크기 : {screen_options[int(screen)]}")
    print(f"제품 색상 : {color_options[int(color)]}")
    print(f"제품 용량 : {memory_options[int(memory)]}")
    print(f"네트워크 : {network_options[int(network)]}")
    print(f"이름 : {name}")
    print(f"시리얼 넘버 : {serial_number}")
    print("-" * 34)

# 프로그램 실행
while True:
    if choice_pad() == "2":
        print("iPad Pro 구입을 종료합니다.")
        break

    screen = select_screen()
    color = select_color()
    memory = select_memory()
    network = select_network()
    name = select_name_service()
    make_ipad(screen, color, memory, network, name)
