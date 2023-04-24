#조기 리턴(early returns); 흐름 중간에 return 키워드를 사용하는 것

#함수를 선언합니다.
def fibonacci(n):
    if n in dictionary:
        #메모되어 있으면 메모된 값을 리턴
        return dictionary[n]
    else:
        #메모되어 있지 않으면 값을 구함
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output
    
#해당 코드를 흐름 중간에 return 키워드를 사용하는 것으로 바꾸게 된다면
#들여쓰기 단계가 줄기 때문에 코드를 더 쉽게 읽을 수 있다.

#함수를 선언합니다.
def fibonacci(n):
    if n in dictionary:
        #메모되어 있으면 메모된 값 리턴
        return dictionary[n]
    #메모되어 있지 않으면 값을 구함
    output = fibonacci(n - 1) + fibonacci(n - 2)
    dictionary[n] = output
    return output


#리스트 평탄화하는 재귀 함수 만들기
#리스트 평탄화; 중첩된 리스트가 있을 때 중첩을 모두 제거하고 풀어서 1차원 리스트로 만드는 것
# q. 다음과 같이 세 번 중첩된 리스트를 평탄화하기 위해서는 어떻게 해야 할까?

#def flatten(data):
    #output = []

    #return output

#def flatten(data):
    #output = []
    #for item in data:

    #return output

#def flatten(data):
    #output = []
    #for item in data:
        #if type(item) == list:

        #else:
            #output.append(item)
    #return output

    #완성된 코드 => 리스트 평탄화하기(1) = list_flatten01.py