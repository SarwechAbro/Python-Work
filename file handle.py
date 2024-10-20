name = 'sarwech abro is here. maan ta second line te likhi rahyo ahyan. and 3rd line te b.'
with open('sample.csv', "w") as f:
    temp = name.replace('.','\n')
    f.writelines(temp)
    print(temp)