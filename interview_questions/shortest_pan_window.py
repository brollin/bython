# Write a function to find the shortest panalphabetic window. A panalphabetic window is a substring containing all letters of an alphabet in the right order.
# e.g.
# Input string = "AxxxxxxBxxxxCxxxADxBCxD"
# Alphabet = [A, B, C, D]
# Windows = ["AxxxxxxBxxxxCxxxAD", "ADxBCxD"]
# Return shortest = "ADxBCxD"


def shortest_panalphabetic_window(alphabet, string):

    if string == "":
        return ""

    left = -1
    right = -1
    end = len(string)

    letters = []

    shortest_window = string + " "
    #import pdb; pdb.set_trace()
    while left < end-len(alphabet):
        # Find new A
        left_check = True
        while left_check:
            left += 1
            if letters:
                del letters[0]

            left_check = left < end-len(alphabet) and string[left:left+1] is not alphabet[0]

        if right < left:
            right = left

        # Find first D that ends a panalphabetic window
        while not alphabet_check(list(string[left:right]), alphabet) and right < end:
            while right < end and (right-left < len(alphabet) or string[right-1:right] is not alphabet[-1]):
                letters.append(string[right:right+1])
                right += 1

        if alphabet_check(letters, alphabet):
            if right - left < len(shortest_window):
                shortest_window = string[left:right]
            
    return shortest_window


def alphabet_check(letters, alphabet):
    alphabet_index = 0

    for i in range(len(letters)):
        if letters[i] == alphabet[alphabet_index]:
            alphabet_index += 1
        if alphabet_index == len(alphabet) and i == len(letters)-1:
            return True

    return False

print shortest_panalphabetic_window(['A','B','C','D'], "ABCDxBCxD")
print shortest_panalphabetic_window(['A','B','C','D'], "AxxxxxxBxxxxCxxxADxBCxD")






















# Attempt duing interview:
def shortest_panalphabetic_window_interview(alphabet, string):
    
    left = 0
    right = 0
    shortest_length = -1
    shortest_window = ''

    while left < len(string) - len(alphabet):
        while string[left] is not alphabet[0] and left <= len(string):
            left += 1
        
        while string[right] is not alphabet[-1] and right <= len(string) \
            and right < left or right - left < len(alphabet):
            right += 1
        
        substring = string[left:right]
        alphabet_counter = 0
        for letter in substring:
            if letter is alphabet[alphabet_counter]:
                alphabet_counter += 1
        if alphabet_counter >= len(alphabet) and (len(substring) < shortest_length or shortest_length is -1):
            shortest_length = len(substring)
            shortest_window = substring
        
        left += 1
        
        
        

