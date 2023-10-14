# To take input from the user
num = int(input("Enter The Number Which Table Do You Want: "))
times = int(input("Enter The Times Of Table: "))


for i in range(1,times+1):
     print(num, 'x', i, '=', num*i)