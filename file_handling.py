import pandas as pd

name = input("Enter Your Name: ")
cast = input("Enter Your Cast: ")
cl = input("Enter Your Class: ")

details = []
details.append([name,cast,cl])
df = pd.DataFrame(details, columns=["Name","Cast","Class"])
df.to_csv("stdada.csv", index=False)   

