from random import randint
import time

# 배열에 10000개의 정수를 삽입
array = []
for _ in range(10000):
    array.append(randint(1,100))

start_time = time.time()

end_time = time.time()

print("time :", end_time - start_time)