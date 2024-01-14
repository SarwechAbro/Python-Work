import string
semester_courses = "Data Structures &, Algorithms Probability, & Statistics Software! Requirement Engineering Human Resouse Management Human Computer Interaction Python"
my_lst = semester_courses.split()
my_list = list(set(my_lst))
my_list = [s.translate(str.maketrans('', '', string.punctuation)) for s in my_list]
print(len(my_list))
for sem in my_list:
    if sem == '':
        my_list.remove(sem)
print(len(my_list))
for sem in my_list:
    print(sem)