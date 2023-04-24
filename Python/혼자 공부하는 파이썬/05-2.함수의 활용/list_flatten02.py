def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)
    return output

example = [[1, 2, 3], 4, [5, 6], 7, [8, 9]]
print("original: ", example)
print("convert: ", flatten(example))


# 1) 함수의 변수는 함수 호출마다 따로따로 만들어진다.
# ; flatten()함수에서 flatten() 함수를 호출했을 때
# ; 변수 output이 계속해서 이어진다고 생각할 수도 있는데
# ; 그건 아니고 함수의 변수는 함수 호출마다 따로 만들어진다.

# 2) 함수가 끝나면(리턴되면) 함수를 호출했던 위치로 돌아온다.
# ; 현재 코드에서는 output += flatten(item) 부분에서 재귀적으로 flatten() 함수를 호출한다.