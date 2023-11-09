from random import*
import os
up = input("Enter Your Password: ")
pas = ['1','2','3','4','5','6','7','8','9']
pw=""
print(len(up))
while pw!=up:
        pw="" 
        for latter in range(len(up)):
              guess_pw = pas[randint(0,8)]
              pw=str(guess_pw)+str(pw)
              print("Cracking Password...")
              os.system("cls")
              print("Your Password Is: ",pw)