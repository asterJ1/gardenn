#입력을 받습니다.
num = input("enter the int> ")
num = int(num)

#조건문을 사용합니다.
if num % 2 == 0:
    #조건이 참일 때, 즉 짝수 조건
    print("it's even")
else:
    #조건이 거짓일 때, 즉 홀수 조건
    print("it's odd")