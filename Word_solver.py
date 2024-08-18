import itertools
import enchant

def possible_words(letters, max_length):
  dict = enchant.Dict('en_US')
  words = set()  
  for length in range(1, max_length + 1):
    for combo in itertools.product(letters, repeat=length):
        word=''.join(combo)
        if dict.check(word):
            words.add(word)
  return words

letters = input("Enter letters of a word without space: ")
result = possible_words(letters, len(letters))
for word in result:
    print(word)
    
print(f"There are {len(result)} possible words from these letters")