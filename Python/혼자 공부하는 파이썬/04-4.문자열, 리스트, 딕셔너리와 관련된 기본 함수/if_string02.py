#변수를 선언합니다.
num = int(input("enter the integer> "))

#if조건문으로 홀수 짝수를 구분합니다.
if num % 2 == 0:
    print("입력한 문자열은 {}입니다.\n{}는(은) 짝수입니다.".format(num, num))
else:
    print("입력한 문자열은 {}입니다.\n{}는(은) 홀수입니다.".format(num, num))