#변수를 선언합니다.
num = int(input("enter the integer> "))

#if 조건문으로 홀수 짝수를 구분합니다.
if num % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 짝수입니다."
    ]).format(num, num))
else:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 홀수입니다."
    ]).format(num, num))