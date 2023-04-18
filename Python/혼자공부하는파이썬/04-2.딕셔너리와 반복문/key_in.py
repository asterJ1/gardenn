#딕셔너리를 선언합니다.
dictionary = {
    "name": "7D dried mango",
    "type": "당절임",
    "ingredient": ["mango", "sugar", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

#사용자로부터 입력을 받습니다.
key = input("> 접근하고자 하는 키: ")

#출력합니다.
if key in dictionary:
    print(dictionary[key])
else:
    print("you are trying to access not existing key")