par = input("Enter A String: ")
head = input("Enter Another String: ")

with open("check.csv", 'a') as file:
    file.write(head)
    file.write(par)