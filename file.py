import time
with open('intro.txt', 'r') as file:
    for word in file: 
     my_list = word.split()
     #print(my_list)
     qu = input("Ask Me Everything: ")
     query = qu.split()
     with open('queries.txt', 'a') as f:
      for que in query:
          f.write(que)
          f.write(" ")
      var = []
     for words in query:
        for lat in my_list:
             if words==lat:
                var.extend(words.split())
                #print(var)
                
for value in set(var):
     count = var.count(value)
     ind = [i for i, x in enumerate(my_list) if x == value]
     value = (value, count ,'times in paragraph on index', ind)
    
     for char in value:
         print(char , end=' ', flush=True)
         time.sleep(0.1)  
         
     print()

