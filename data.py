import pandas as pd
data = []
option = "y"
while True:
    if option != 'n':
        name = input("Name: ")
        fname = input("Father Name: ")
        add = input("Address: ")
        data.append([name.capitalize(), fname.capitalize(), add.capitalize()])
        option = input("Do you want add another data [y/n]: ")
    else:
        print("Data saved in students.csv in same directory")
        break



df = pd.DataFrame(data=data)
df.to_csv("Students.csv", index=False, mode="a", header=False)