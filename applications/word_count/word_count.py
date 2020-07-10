def word_count(s):
    # Your code here
    words = {}
    ignored_characters = {"\"": None, ":": None, ";": None, ",": None, ".": None, "-": None, "+": None, "=": None, "/": None, "\\": None, "|": None, "[": None, "]": None, "{": None, "}": None, "(": None, ")": None, "*": None, "^": None, "&": None}
    s = s.lower().strip()
    for l in s:
        if l in s:
            if l in ignored_characters:
                s = s.replace(l, "")
    s = s.split()
    for w in s:
        if w  not in words:
            words[w] = 1
        else:
            words[w] += 1
    return words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
