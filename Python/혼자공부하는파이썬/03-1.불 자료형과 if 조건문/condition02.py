#입력을 받습니다.
num = input("enter integer> ")
last_ch = num[-1]

#짝수 조건
if last_ch in "02468":
    print("it is even")

#홀수 조건
if last_ch in "13579":
    print("it is odd")