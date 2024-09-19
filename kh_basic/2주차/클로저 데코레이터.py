# 클로저 = 함수 안에 내부 함수를 구현하는 것
# 객체 지행 언어에서 생성된 객체 내부의 메서드가 필드를 참조하는 것과 유사
from websocket import WebSocket


def calc() :
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b
    return mul_add

c = calc()
print(c(1), c(2), c(3), c(4), c(5))

# 콜백 기능 구현
import time

def perform_operation(x, y, callback):
    result = 0
    for i in range(x) :
        result += i + x + y
        time.sleep(1)
    callback(result)  # 콜백 함수 호출:

# 콜백 함수 정의
def callback_function(result):
    print(f"Operation result is: {result}")

# perform_operation 함수를 호출하면서 콜백 함수를 전달
perform_operation(10, 20, callback_function)


# 데코레이터 /함수의 앞 뒤에 기능을 추가할 때 사용
import datetime

def datetime_deco(func):
    def decorated():
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
    return decorated

@datetime_deco
def for_sum():
    sum = 0
    for i in range(1, 100000):
        sum += i
    print(sum)

# 첫번째 방법
test = datetime_deco(for_sum)
test()

# 두번째 방법
# for_sum()
