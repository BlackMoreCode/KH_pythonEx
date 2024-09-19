# 함수로 영화표 얘마하기
# 사용자로부터 좌석번호를 입력 받아 예매하는 시스템. 좌석은 10개
# 좌석 값은 얘매 전은 0, 얘매 완료시 1로 변경 (즉 초기 값은 0)
# 이미 예매가 완료된 좌석은 재구매 불가
# 좌석당 가격은 12000 won.

seat = [0] * 10 # 0으로 초기화된 10개의 리스트 생성
PRICE = 12000

def print_seat():
    for e in seat:
        if e == 0:
            print("[ ]", end=" ")
        else:
            print("[V]", end=" ")
    print()

print_seat()

def select_seat(): # 좌석 예매 관련 함수
    print_seat()
    num = int(input("좌석 번호 입력 : ")) - 1 # 사용자의 입력은 1부터 시작, 리스트 인덱스는 0부터 시작. 그러므로 -1 필요.
    if seat[num] == 0:
        seat[num] = 1 #예약이 안된 좌석이므로 예약을 진행
        print_seat()
    else:
        print("이미 예약된 좌석입니다")

def total_account():
    cnt = 0 # 판매된 좌석의 수를 누적하기 위한 변수
    for e in seat:
        if e == 1: cnt += 1
    return PRICE * cnt # 티켓 가격 + 판매 좌석

while True:
    print("[1] 예매하기")
    print("[2] 종료하기")
    sel = int(input("메뉴선택 : "))
    if sel == 1: select_seat()
    else:
        print(f"총 매출액 : {total_account()}")
        break