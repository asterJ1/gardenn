array = [273, 32, 103, "string", True, False]
print(array)

#리스트 선언하고 요소에 접근하기
[1, 2, 3, 4]
["안", "녕", "하", "세", "요"]
[273, 32, 103, "string", True, False]

list_a = [273, 32, 103, "string", True, False]
list_a[0]
list_a[1]
list_a[2]
list_a[1:3]

list_a = [273, 32, 103, "string", True, False]
list_a[0] = "change"
list_a

#첫째, 대괄호 안에 음수를 넣어 뒤에서부터 요소를 선택할 수 있습니다.
list_a = [273, 32, 103, "string", True, False]
list_a[-1]
list_a[-2]
list_a[-3]

#둘째, 리스트 접근 연산자를 다음과 같이 이중으로 사용할 수 있습니다.
list_a = [273, 32, 103, "string", True, False]
list_a[3]
list_a[3][0]

#셋째, 리스트 안에 리스트를 사용할 수도 있습니다.
list_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_a[1]
list_a[1][1]

#리스트에서의 IndexError 예외
list_a = [273, 32, 103]
#list_a[3] <- 범위 바깥의 인덱스임 하고 에러 뜸

#리스트에 요소 추가하기: append(), insert(), extend()
list_a = [1, 2, 3]
list_a.extend([4, 5, 6])
print(list_a)

#리스트 연결 연산자와 요소 추가의 차이
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_a + list_b
list_a
list_b

list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_a.extend(list_b)
list_a
list_b

#인덱스로 제거하기: del 키워드, pop()
list_b = [0, 1, 2, 3, 4, 5, 6]
del list_b[3:6]
list_b

list_c = [0, 1, 2, 3, 4, 5, 6]
del list_c[:3]
list_c

list_d = [0, 1, 2, 3, 4, 5, 6]
del list_d[3:]
list_d

#값으로 제거하기: remove()
list_c = [1, 2, 1, 2]
list_c.remove(2)
list_c

#모두 제거하기: clear()
list_d = [0, 1, 2, 3, 4, 5]
list_d.clear()
list_d

#리스트 정렬하기: sort()
list_e = [52, 273, 103, 32, 275, 1, 7]
list_e.sort() #오름차순 정렬
list_e
list_e.sort(reverse = True) #내림차순 정렬
list_e

#리스트 내부에 있는지 확인하기: in/not in 연산자
list_a = [273, 32, 103, 57, 52]
273 in list_a
99 in list_a
100 in list_a
52 in list_a

list_a = [273, 32, 103, 57, 52]
273 not in list_a
99 not in list_a
100 not in list_a
52 not in list_a
not 273 in list_a 
#물론 in 연산자를 사용하고 전체를 not으로 감싸는 방법도 사용할 수 있지만,
#not in 연산자를 사용하는 것이 훨씬 읽기 쉽습니다.

#for 반복문
print("output")
print("output")
print("output")
print("output")
print("output")

for i in range(7):
    print("output")

#중첩 리스트와 중첩 반복문
list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

#좀 더 알아보기: 전개 연산자
#첫째, 리스트 내부에 사용하는 경우
a = [1, 2, 3, 4]
b = [*a, *a]
b

#append() 함수를 사용한 경우
a = [1, 2, 3, 4]
a.append(5)
a

#전개 연산자를 사용한 경우
b = [1, 2, 3, 4]
c = [*b, 5]
b
c

#둘째, 함수 매개변수 위치에 사용하는 경우
a = [1, 2, 3, 4]
print(*a)