
with open('Newzealand lost.txt', 'r') as file:
    for word in file: 
     my_list = word.split()
     #print(my_list)
     qu = input("Enter A word which Do You Want To Find: ")
     query = qu.split()
     #print(query)
     var = []
     for words in query:
        for lat in my_list:
             if words==lat:
                var.extend(words.split())
                #print(var)
                
for value in set(var):
     count = var.count(value)
     ind = [i for i, x in enumerate(my_list) if x == value]
     print(value, count ,'times in history on index', ind)
     
     
