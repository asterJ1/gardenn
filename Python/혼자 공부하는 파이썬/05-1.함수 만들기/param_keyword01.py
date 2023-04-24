def print_n_times(*value, n=2):
    #n번 반복합니다.
    for i in range(n):
        #values는 리스트처럼 활용합니다.
        for value in values:
            print(value)
        #단순한 줄바꿈
        print()

#함수를 호출합니다.
print_n_times("hello", "funny", "Python Programming", n=3) #n=3은 키워드 매개변수이다.
#키워드 매개변수; 매개변수 이름을 지정해서 입력하는 매개변수