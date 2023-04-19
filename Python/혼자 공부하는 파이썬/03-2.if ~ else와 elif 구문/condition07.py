#변수를 선언합니다.
score = float(input("학점 입력> "))

#조건문을 적용합니다.
if score == 4.5:
    print("god")
elif 4.2 <= score:
    print("the love of professor")
elif 3.5 <= score:
    print("protector of this system")
elif 2.8 <= score:
    print("ordinary person")
elif 2.3 <= score:
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= score:
    print("오락문화의 선구자")
elif 1.0 <= score:
    print("불가촉천민")
elif 0.5 <= score:
    print("자벌레")
elif 0 < score:
    print("플랑크톤")
else:
    print("시대를 앞서가는 혁명의 씨앗")   