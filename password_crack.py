from random import randint
import os
import time
up = input("Enter Your Password: ")
pas = ['5','1','9','6','2','0','4','8','3','7']
pw=""
#print(len(up))
while pw!=up:
        pw="" 
        for latter in range(len(up)):
              guess_pw = [pas[randint(0,9)] for _ in range(len(up))]
              pw = ''.join(guess_pw)
              print('cracking password....', pw)
              os.system("cls")
             
print("Your Password Is: ",  end='',)            
for char in pw:
       print(char , end='', flush=True)
       time.sleep(0.6)              
            