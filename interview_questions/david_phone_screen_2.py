def find_words(string, words, memo):
    if string in words:
        return string
    if string in memo:
       return "empty string"

    word = ""
    for i, letter in enumerate(string):
        word = string[:i+1]
        
        if word in words:
            if i == len(string)-1:
                return string
            remaining_words = find_words(string[i+1:], words, memo)
            if remaining_words is not "empty string":
                return " ".join([word, remaining_words])

    memo[string] = None

    return "empty string"

def find_two_words(string, words):
    
    word = ""
    for i,letter in enumerate(string):
        word = string[:i+1]

        if word in words:
            if i == len(string)-1:
                return string
            if string[i+1:] in words:
                return " ".join([string[:i+1], string[i+1:]])

    return "empty string"

words = ('apple', 'pie', 'shorter', 'the', 'cat')

print find_two_words('applepie',words)
print find_two_words('shorter',words)
print find_two_words('asdx',words)

print find_words('applepiethecat', words, {})
print find_words('shorter', words, {})
print find_words('asdx', words, {})

words = []
for i in range(1,101):
    words.append('a'*i)
words = set(words)

print find_words('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', words, {})

