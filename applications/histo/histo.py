# Your code here


def countWords(file):
    ignoredCharacters = '":;,.-+=/\|[]{}()*^&?!'

    wordMap = {}

    with open(file) as f:
        words = f.read().lower()
        for char in ignoredCharacters:
            words = words.replace(char, "")
        words = words.split()

    for word in words:
        if word not in wordMap:
            wordMap[word] = 1
        else:
            wordMap[word] += 1
    return wordMap
    

def renderWordCount(dic):
    counts = [(dic[word], word) for word in dic]
    counts.sort(key = lambda e: (-e[0], e[1]))
    maxLength = 0

    for word in counts:
        if len(word[1]) > maxLength:
            maxLength = len(word[1])
        
    for word in counts:
        print(f'{word[1]}\t'.expandtabs(maxLength + 2) + "#" * word[0])

    






renderWordCount(countWords("robin.txt"))