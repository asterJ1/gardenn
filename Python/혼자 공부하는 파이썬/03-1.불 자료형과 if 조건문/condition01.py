#입력을 받습니다.
num = input("enter integer> ")

#마지막 자리 숫자를 추출
last_ch = num[-1]

#숫자로 변환하기
last_ch = int(last_ch)

#짝수 확인하기
if last_ch == 0 \
    or last_ch == 2 \
    or last_ch == 4 \
    or last_ch == 6 \
    or last_ch == 8:
    print("it is even")

#홀수 확인하기
if last_ch == 1 \
    or last_ch == 3 \
    or last_ch == 5 \
    or last_ch == 7 \
    or last_ch == 9:
    print("it is odd")