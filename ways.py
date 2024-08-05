from random import*
import math
from AyDictionary import AyDictionary
i = 0
my_elements = input("Enter latters of a word with space: ").split()
print(my_elements)
element_to_show = len(my_elements)
ways = (math.factorial(len(my_elements)) / math.factorial(len(my_elements) - element_to_show))
data1 = ''
final = []
for way in range(int(ways)):
     data =  [my_elements[randint(0,len(my_elements)-1)] for _ in range(element_to_show)]
     data1 = ''.join(data).lower()
     if data1 not in final:
           final.append(data1)
     i+=1
dict = AyDictionary()       
for data in final:
    #print(data)
    for word in dict:
        if word == data:
            print(word)
    
    

print("loop run times {}".format(i))