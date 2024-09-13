#날짜와 시감 관련 함수
from datetime import datetime # dateitem 모듈에서 datetime 함수를 가져온다

print(datetime.today())
print(datetime.today().month)
print(datetime.today().date())
print(datetime.today().time())
print(datetime.today().hour)

import calendar
# print(calendar.calendar(2024))

# math 모듈 : 수학 관련 기능
import math

print(math.sin(1))
print(math.cos(1))
print(math.tan(1))
print(math.ceil(1.0000000000001)) # 소수점 이하 있을 시 무조건 올림
print(math.floor(1.999999999999)) # 소수점 이하는 무조건 날림