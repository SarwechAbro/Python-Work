from random import randint
import os
import time
up = input("Enter Your Password: ")
pas = ['0','1','2','3','4','5','6','7','8','9']
pw=""
coun=0
#print(len(up))
while pw!=up:
        pw="" 
        for latter in range(len(up)):
              guess_pw = [pas[randint(0,len(pas)-1)] for _ in range(len(up))]
              pw = ''.join(guess_pw)
              print('cracking password....', pw)
              coun+=1
              os.system("clear")
             
print("Your Password Is: ",  end='',)            
for char in pw:
       print(char , end='', flush=True)
       time.sleep(0.6) 

print(f"\nloop times {coun}")