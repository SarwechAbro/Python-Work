import time
with open('intro.txt', 'r') as file:
    for word in file: 
        my_list = word.split()
        #print(my_list)
qu = input("Ask Me Something: ")
query = qu.split()
with open('queries.txt', 'a') as f:
    for que in query:
        f.write(f'{que} ')
var = []
coun = 0 
for words in query:
    for lat in my_list:
        if words==lat:
            var.extend(words.split())
        coun+=1
for value in set(var):
    count = var.count(value)
    ind = [i for i, x in enumerate(my_list) if x == value]
    tuple = (value,'is', count ,'time(s) in paragraph on index', ind)
    for char in tuple:
        print(char , end=' ', flush=True)
        time.sleep(0.1)  
    print()
print(f"loop times {coun}")

