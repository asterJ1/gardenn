#딕셔너리 선언하기
dict_a = {
    "name": "avengers endgame",
    "type": "hero movie"
}

#딕셔너리의 요소에 접근하기
dict_a

dict_a["name"]
dict_a["type"]

dict_b = {
    "director": ["anthony russo", "joe russo"],
    "cast": ["ironman", "thanos", "doctor strange", "hulk"]
}

dict_b
dict_b["director"]

#딕셔너리의 문자열 키와 관련된 실수 - 예외 처리
#dict_key ={
    #name = "7D dried mango",
    #type: "당절임"
#}
#name이라는 이름이 정의되지 않았다는 오류:
#아래와 같이 name이라는 이름을 변수로 만들어 주면 됨

name = "이름"
dict_key = {
    name: "7D dried mango",
    type: "당절임"
}
dict_key

#KeyError 예외 - 예외 처리
#dictionary = {}
#dictionary["Key"]
#리스트의 길이를 넘는 인덱스에 접근하면 IndexError이 발생함
#또한 딕셔너리도 존재하지 않는 키에 접근하면 마찬가지로 KeyError이 발생함

#del dictionary["Key"]
#값을 제거할 때에도 마찬가지