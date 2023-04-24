#함수를 선언합니다.
def sum_all(start, end):
    #변수를 선언합니다.
    output = 0
    #반복문을 돌려 숫자를 더합니다.
    for i in range(start, end + 1):
        output += i
    #리턴합니다.
    return output

#함수를 호출합니다.
print("a.", sum_all(0, 100, 10))
print("b.", sum_all(end=100))
print("c.", sum_all(end=100, step=2))