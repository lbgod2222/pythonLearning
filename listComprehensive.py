# 列表表达式效率测试
import time as time
start1 = time.time()
print(sum([i for i in range(1,100000000) if i%3==0 or i%5==0]))
end1 = time.time()
print('Process 1 end, total cost:', end1 - start1)
start2 = time.time()
print(sum((i for i in range(1,100000000) if i%3==0 or i%5==0)))
end2 = time.time()
print('Process 2 end, total cost:', end2 - start2)

'''
Process 1 cost 10.272 seconds
Process 2 cost 9.895 seconds
'''