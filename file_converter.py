import pandas as pd
file = input("Enter File Name: ")
ext = input("File Extension: ")
if ext.endswith("csv"):
    data = pd.read_csv(f"{file}.{ext}")
elif ext.endswith("json"):
    data = pd.read_json(f"{file}.{ext}")
outfile = input("Enter formate which you want your file in (Ex json): ")
ind = input("Index (true/false): ").capitalize()
df = pd.DataFrame(data=data)
if outfile == "json":
    format = input("formate (columns, values, records, table): ")
    df.to_json(f"{file}.{outfile}", index=ind, orient=format)
elif outfile == "csv":
    df.to_csv(f"{file}.{outfile}", index=ind)
elif outfile == "html":    
    df.to_html(f"{file}.{outfile}", index=ind)
print(ind)    