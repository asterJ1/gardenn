#딕셔너리를 선언합니다.
dictionary = {
    "name": "7D dried mango",
    "type": "당절임",
    "ingredient": ["mango", "sugar", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

#존재하지 않는 키에 접근해 봅니다.
value = dictionary.get("존재하지 않는 키")
print("value: ", value)

#None 확인 방법
if value == None: #None과 같은지 확인만 하면 됨
    print("존재하지 않는 키에 접근했었습니다.")