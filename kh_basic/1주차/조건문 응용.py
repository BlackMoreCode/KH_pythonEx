# 회원가입을 위한 ID/PW 받기
id = input("ID입력 : ")

if len(id) >= 8:
    pw = input("비밀번호 입력 : ")
    if len(pw) < 8 or len(pw) > 16 :
        print("비밀번호는 8~16자리 사이여야 합니다")
    elif pw.find(id) >= 0: #id랑 pw를 같은 값을 쓸 시를 찾아내는 조건문
        print("PW에 ID 값을 쓸 수 없습니다")
    else:
        print(f"ID: {id}")
        print(f"PW: {pw}")
else:
    print("아이디는 8자리 이상이여야 합니다.")

# 아르바이트 급여 계산
# 주간 근무 시급: 9860 원
# 야근 근무 시급 : 주간 * 1.5
# [출력] 주간 근무 [1] 입력, 야간 근무 [2] 입력
# [출력] 근무 시간을 입력
# [출력] print(f"{근무시간} 동안 근무한 {근무 타입} 급여는 {급여} 원 입니다)

wage = 9860
night_wage = wage * 1.5

work_type = int(input("주간근무는 1, 야간근무는 2를 입력하세요: "))
working_hrs =  int(input("근무시간 : "))

if work_type == 1:
    payment = wage * working_hrs
# else : payment = night_wage * working_hrs
elif work_type == 2 :
    payment = night_wage * working_hrs
else :
    print("are you sure about this?")
    exit()

work_type_str = work_type == 1 and "주간" or "야간"

print(f"{working_hrs}시간 동안 근무한 {work_type_str} 급여는 {payment}원 입니다")