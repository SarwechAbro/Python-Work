from random import*
import os
up = input("Enter Your Password: ")
pas = ['9','3','1','4','6','8','5','7','2']
pw=""
#print(len(up))
while pw!=up:
        pw="" 
        for latter in range(len(up)):
              guess_pw = pas[randint(0,8)]
              pw=str(guess_pw)+str(pw)
              #os.system("cls")
              print("Your Password Is: ",pw)
              f = open("password.txt","w")
              f.write(pw)
             