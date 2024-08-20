import itertools
import enchant


i = 0
dict = enchant.Dict('en_US')
words = set() 
letters = input("Enter letters without space: ") 
min = int(input("Enter minimum number of latters of word: "))
for length in range(1,  len(letters) + 1):
    for combo in itertools.product(letters, repeat=length):
        word=''.join(combo)
        if dict.check(word):
          words.add(word)
        i+=1
list_words = list(words)
sorted_words = sorted(list_words)
for word in sorted_words:
  if len(word) >= min:
    print(word)
    
print(f"There are {len(words)} possiblities of correct words from these letters")
print(f"There are {i} possible combinations can be arranged from these letters")
