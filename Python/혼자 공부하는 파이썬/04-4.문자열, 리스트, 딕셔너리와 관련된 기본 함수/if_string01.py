#변수를 선언합니다.
num = int(input("enter the integer> "))

#if 조건문으로 홀수 짝수를 구분합니다.
if num % 2 == 0:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 홀수입니다.""".format(num, num))
    
else:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 홀수입니다.""".format(num, num))

#예상치 못 한 들여쓰기가 문자열에 들어갑니다.