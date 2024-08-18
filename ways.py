import enchant
from itertools import permutations

latters = input("Enter latters of a word with space: ").split()
i = 0
final = []
permutations_list = list(permutations(latters))

for permutation in permutations_list:
  data = ''.join(permutation)
  i+=1
  if data not in final:
    final.append(data)
dict = enchant.Dict('en_US')    
for word in final:
    #print(word)
    is_eng_word = dict.check(word)
    #print(is_eng_word) 
    if is_eng_word:
        print(word)
print(f'there are {i} posibilties of words from these latters')
    
