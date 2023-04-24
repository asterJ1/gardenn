#변수를 선언합니다.
nums = [5, 15, 6, 20, 7, 25]

#반복을 돌립니다.
for num in nums:
    #num가 10보다 작으면 다음 반복으로 넘어갑니다.
    if num < 10:
        continue
    #출력합니다.
    print(num)