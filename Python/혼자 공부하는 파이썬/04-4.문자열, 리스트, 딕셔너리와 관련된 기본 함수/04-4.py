#리스트에 적용할 수 있는 기본 함수: min(), max(), sum()
nums = [103, 52, 273, 32, 77]
min(nums)

max(nums)

sum(nums)

#리스트를 사용하지 않고 최솟값, 최댓값 구하기
min(103, 52, 273)
max(103, 52, 273)

temp = reversed([1, 2, 3, 4, 5, 6])

for i in temp:
    print("첫 번째 반복문: {}".format(i))

for i in temp:
    print("두 번째 반복문: {}".format(i))

nums = [1, 2, 3, 4, 5, 6]

for i in reversed(nums):
    print("첫 번쨰 반복문: {}".format(i))

for i in reversed(nums):
    print("두 번째 반복문: {}".format(i))

#enumerate() 함수와 반복문 조합하기
#sol.1
example_list = ["요소A", "요소B", "요소C"]
i = 0
for item in example_list:
    print("{}번쨰 요소는 {}입니다.".format(i, item))
    i += 1

#sol.2
example_list = ["요소A", "요소B", "요소C"]
for i in range(len(example_list)):
    print("{}번째 요소는 {}입니다.".format(i, example_list))

#문자열의 join() 함수
print("::".join(["1", "2", "3", "4", "5"]))