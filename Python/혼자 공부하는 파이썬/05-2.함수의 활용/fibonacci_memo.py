#메모 변수를 만듭니다.
dictionary = {
    1: 1,
    2: 1
}

#함수를 선언합니다.
def fibonacci(n):
    if n in dictionary:
        #메모가 되어 있으면 메모된 값을 리턴
        return dictionary[n]
    else:
        #메모가 되어 있지 않으면 값을 구함
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output

#함수를 호출합니다.
print("fibonacci(10): ", fibonacci(10))
print("fibonacci(20): ", fibonacci(20))
print("fibonacci(30): ", fibonacci(30))
print("fibonacci(40): ", fibonacci(40))
print("fibonacci(50): ", fibonacci(50))

#메모(memo): 딕셔너리를 사용해서 한 번 계산한 값을 저장하는 것
# ;딕셔너리에 값이 메모되어 있으면 처리를 수행하지 않고 곧바로 메모된 값을 돌려주면서
# ;코드의 속도를 빠르게 만드는 것
#메모화를 사용하면 실행 후 곧바로 결과를 출력할 정도로 속도가 빨라진다.
#재귀 함수와 함께 많이 사용되는 기술이다.