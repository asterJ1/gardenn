#범위
a = range(5)
a
list(range(5))

list(range(0, 5))#0부터 (5-1)까지의 정수로 범위를 만듭니다.
list(range(5, 10))#5부터 (10-1)까지의 정수로 범위를 만듭니다.

list(range(0, 10, 2))#0부터 2씩 증가하면서 (10-1)까지의 정수로 범위를 만듭니다.
list(range(0, 10, 3))#0부터 3씩 증가하면서 (10-1)까지의 정수로 범위를 만듭니다.

a = range(0, 10 + 1)
list(a)

n = 10
#a = range(0, n / 2) <- 매개변수로 나눗셈을 사용한 경우 오류발생
#TypeError가 발생하는 이유: range() 함수의 매개변수로는 반드시 '정수'를 입력해야 하기 떄문

a = range(0, int(n / 2))
list(a)
a = range(0, n // 2)
list(a)

#for 반복문: 리스트와 범위 조합하기
#리스트를 선언합니다.
array = [273, 32, 103, 57, 52]
#리스트에 반복문을 적용합니다.
for element in array:
    #출력합니다.
    print(element)

#while 반복문: 시간을 기반으로 반복하기
#import time
#time.time()