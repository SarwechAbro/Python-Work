from collections import Counter

def most_common(lst):
    data = Counter(lst)
    return data.most_common(1)[0][0]

words = []
with open('queries.txt', 'r') as file:
    for query in file:
        words.extend(query.split())

count = words.count(most_common(words))
ind = [i for i, x in enumerate(words) if x == (most_common(words))]
print('most searched query in history is',most_common(words),'it is', count ,'times used in paragraph on index', ind)
