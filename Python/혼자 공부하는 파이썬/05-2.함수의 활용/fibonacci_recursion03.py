#UnboundLocalError에 대한 처리
#왜 global counter이라는 코드를 썼을까?
# => 파이썬은 함수 내부에서 함수 외부에 있는 변수를 참조하지 못한다.
#참조: 변수에 접근하는 것.
# => 따라서 함수 내부에서 함수 외부에 있는 변수라는 것을 설명하기 위해서는 global 키워드를 사용해야 한다.
#global 키워드는 파이썬 프로그래밍 언어에만 있는 특이한 구조이다.

#변수를 선언합니다.
counter = 0

#함수를 선언합니다.
def fibonacci(n):
    counter += 1
    #피보나치 수를 구합니다.
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
#함수를 호출합니다.
print(fibonacci(10))