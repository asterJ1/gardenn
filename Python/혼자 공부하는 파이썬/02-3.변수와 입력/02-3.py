#변수 만들기/사용하기
pi = 3.14159265
print(pi)
print(pi + 2)
print(pi - 2)
print(pi / 2)
print(pi % 2)
print(pi * pi)

#복합 대입 연산자
number = 100
number += 10
number += 20
number += 30
print("number: ", number)

string = "안녕하세요"
string += "!"
string += "!"
print("string: ", string)

#사용자 입력: input()
#input() 함수로 사용자 입력받기
input("인사말을 입력하세요> ")

string = input("인사말을 입력하세요> ")
print(string)

#input() 함수의 입력 자료형
print(type(string))

number = input("숫자를 입력하세요> ")
print(number)

print(type(number))