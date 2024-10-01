name = ['sarwech', 'abro', "work", "not", "his", 'pip']
with open('sample.csv', "w") as f:
    for n in name:
        f.write(n + "\n")