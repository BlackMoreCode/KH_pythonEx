# 대소문자 바꾸기 upper(), lower()
a = "Hello Python Program..."
print(a.upper())
print(a.lower())

# for 문 사용.
# isLower() : 소문자면 true 반환, 아닐 시 false 반환

#psuedo: for 문 if 조건문 사용해서 조건 체크.

rst = ""
for e in input():
    if e.islower():
        rst += e.upper()
    else:
        rst += e.lower()
print(rst)


# 2번째 방법은 걍 swapcase 메서드 사용
b = a.swapcase()
print(b)
