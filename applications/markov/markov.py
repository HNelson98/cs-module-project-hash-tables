import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    splitWords = words.split()


# TODO: analyze which words can follow other words
# Your code here
mark_storage = dict()
startWords = list()
endWords = list()
capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '"']
ends = ['.', '?', '!', '"']

for i in range(len(splitWords) - 1):
    if splitWords[i][0] in capitals:
        startWords.append(splitWords[i])
    if splitWords[i][-1] in ends:
        endWords.append(splitWords[i])
    mark_storage[splitWords[i]] = mark_storage.get(splitWords[i], [])
    mark_storage[splitWords[i]].append(splitWords[i + 1])

# print(endWords)


# TODO: construct 5 random sentences
# Your code here
for i in range(5):
    sentence = ""
    start = random.choice(startWords)
    sentence += start + " " 
    next_Word = random.choice(mark_storage[start])
    while start not in endWords:
        if next_Word in endWords:
            sentence += next_Word
            break
        sentence += next_Word + " "
        next_Word = random.choice(mark_storage[next_Word])
    print(sentence)
