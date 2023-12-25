import pandas as pd
name = input('Enter Your Name: ')
data= []
topic = 'name'
namea = name.strip('.')
s_name = namea.split('.')
for n in s_name:
    data.append([topic,n])

print(data)
df = pd.DataFrame(data, columns=["Titles", "Headings"])
df.to_csv("example.csv", index=False)
