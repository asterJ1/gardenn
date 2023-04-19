#딕셔너리를 선언합니다.
dictionary = {
    "name": "7D dried mango",
    "type": "당절임",
    "ingredient": ["mango", "sugar", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

#for 반복문을 사용합니다.
for key in dictionary:
    #출력합니다.
    print(key, ":", dictionary[key])