#딕셔너리를 선언합니다.
dictionary = {
    "name": "7D dried mango",
    "type": "당절임",
    "ingredient": ["mango", "sugar", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

#출력합니다.
print("name: ", dictionary["name"])
print("type: ", dictionary["type"])
print("ingredient: ", dictionary["ingredient"])
print("origin: ", dictionary["origin"])
print()

#값을 변경합니다.
dictionary["name"] = "8D dried mango"
print("name: ", dictionary["name"])

#딕셔너리에 값 추가하기/제거하기
dictionary["price"] = 5000
dictionary

#기존의 값을 새로운 값으로 대치
dictionary["name"] = "8D dried pineapple"
dictionary

#딕셔너리 요소의 제거 - del 키워드 활용
del dictionary["ingredient"]
dictionary