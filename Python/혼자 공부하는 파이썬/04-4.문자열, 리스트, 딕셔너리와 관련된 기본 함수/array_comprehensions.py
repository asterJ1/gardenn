#리스트를 선ㅓ합니다.
array = ["apple", "plum", "chocolate", "banana", "cherry"]
#array의 요소를 fruit이라고 할 때 chocolate이 아닌 fruit으로 리스트를 재조합해주세요.
output = [fruit for fruit in array if fruit != "chocolate"]

#출력합니다.
print(output)