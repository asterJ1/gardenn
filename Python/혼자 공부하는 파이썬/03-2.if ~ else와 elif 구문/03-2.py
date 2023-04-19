#입력을 받습니다.
num = input("정수 입력> ")
num = int(num)

#짝수 조건
if num % 2 == 0:
    print("it's even")

#홀수 조건
if num % 2 == 1:
    print("it's odd")

#raise NotlmplementedError
#입력을 받습니다.
num = input("enter the integer> ")
num = int(num)

#조건문 사용
if num > 0:
    #양수일 떄: 아짖ㄱ 미궇현 상태입니다.
    raise NotImplementedError
else:
    #음수일 때: 아직 미구현 상태입니다.
    raise NotImplementedError