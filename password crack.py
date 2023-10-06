from random import*
import os
up = input("Enter Your Password: ")
pas = ['s','a','r','w','e','c','h','a','b','r','o','1','1','0','@','%','$']
pw=""
print(len(up))
while pw!=up:
        pw="" 
        for latter in range(len(up)):
              guess_pw = pas[randint(0,16)]
              pw=str(guess_pw)+str(pw)
              print("Cracking Password... Please Wait...")
              os.system("cls")
              print("Your Password Is: ",pw)