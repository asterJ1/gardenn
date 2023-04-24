def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += item
        else:
            output.append(item)

    return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("original: ", example)
print("convert: ", flatten(example))

#리스트 변환 결과: [1, 2, 3, 4, [5, 6], 7, 8, 9]
#중간에 [5, 6]이라는 리스트까지 해제하려면
#output += item으로 요소를 추가할 때에도(5번 행) flatten() 함수를 적용해서
#코드를 output += flatten(item)으로 변경하면 된다.
# => list_flatten02.py