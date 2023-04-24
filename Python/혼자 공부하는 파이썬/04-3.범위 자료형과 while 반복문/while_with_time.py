#시간과 관련된 기능을 가져옵니다.
import time

#변수를 선언합니다.
num = 0

#5초 동안 반복합니다.
target_tick = time.time() + 5
while time.time() < target_tick:
    num += 1

#출력합니다.
print("5초 동안 {}번 반복했습니다.".format(num))