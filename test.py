import time

x = 1234567891234567891234567895768687997978

# 使用 >> 操作
start_time = time.time()
for _ in range(100000000):
    result_shift = x >> 9
print("Time for >>:", time.time() - start_time)

# 使用 // 操作
start_time = time.time()
for _ in range(100000000):
    result_divide = x // 512
print("Time for //:", time.time() - start_time)