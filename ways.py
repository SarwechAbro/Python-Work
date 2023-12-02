from random import*
import math
i = 0
my_elements = ['a','b','c','d','e','f']
element_to_show = 4
ways = (math.factorial(len(my_elements)) / math.factorial(len(my_elements) - element_to_show))
data1 = ''
final = []
for way in range(int(ways)):
     data =  [my_elements[randint(0,len(my_elements)-1)] for _ in range(element_to_show)]
     data1 = ''.join(data)
     if data1 not in final:
           final.append(data1)
     i+=1
     
for data in final:
    print(data)

print("loop run times {}".format(i))