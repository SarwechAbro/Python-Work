from random import*
import math
i = 0
my_num = ['a','b','c','d','e']
ways = math.factorial(len(my_num))
data1 = ''
final = []
for way in range(ways):
     data =  [my_num[randint(0,4)] for _ in range(3)]
     data1 = ''.join(data)
     final.append(data1)
     i+=1
     
for data in final:
    print(data)

print("loop run times {}".format(i))