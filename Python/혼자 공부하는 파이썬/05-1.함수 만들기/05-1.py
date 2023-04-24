#매개변수와 관련된 TypeError
def print_n_times(value, n):
    for i in range(n):
        print(value)

#함수를 호출합니다.
#print_n_times("hello")
#함수에 매개변수를 두 개 지정했는데 호출할 때에는 하나만 넣으면
#프로그램은 함수의 매개변수가 없다고 오류를 발생시킨다.

def print_n_times(value, n):
    for i in range(n):
        print(value)

#함수를 호출합니다.
#print_n_times("hello", 10, 20)
#함수에 매개변수를 두 개 지정했는데 호출할 때에 세 개를 넣으면
#프로그램은 지정된 함수의 매개변수보다 많이 들어왔다고 오류를 발생시킨다.

#키워드 매개변수
#기본 매개변수가 가변 매개변수보다 앞에 올 때
#.=>매개변수가 순서대로 입력되므로 n에는 "hello"가 들어가고,
#values에는 ["funny", "Python Programming"]이 들어간다.
#그런데 range() 함수의 매개변수에는 숫자만 들어갈 수 있으므로 오류가 발생한다.

#def print_n_times(n=2, *values):
    #n번 반복합니다.
    #for i in range(n):
        #values는 리스트처럼 활용합니다.
        #for value in values:
            #print(value)
        #단순한 줄바꿈
        #print()

#함수를 호출합니다.
#print_n_times("hello", "funny", "Python Programming", 3)


#가변 매개변수가 기본 매개변수보다 앞에 올 때
#코드를 실행하면 가변 매개변수가 우선된다.
def print_n_times(*values, n=2):
    #n번 반복합니다.
    for i in range(n):
        #values는 리스트처럼 활용합니다.
        for value in values:
            print(value)
        #단순한 줄바꿈
        print()

#함수를 호출합니다.
print_n_times("hello", "funny", "Python Programming", 3)


#키워드 매개변수;
#가변 매개변수와 기본 매개변수를 함께 사용할 수 있는 방법

#while 반복문을 사용합니다.
while True:
    #"."을 출력합니다.
    #기본적으로 end가 "\n"이라 줄바꿈이 일어나는데
    #빈 문자열 ""로 바꿔서 줄바꿈이 일어나지 않게 합니다.
    print(".", end="") #end=""는 키워드 매개변수이다.


#리턴

#input() 함수의 리턴값을 변수에 저장합니다.
value = input("> ")

#출력합니다.
print(value)