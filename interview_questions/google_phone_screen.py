# Write a function to find the shortest panalphabetic window. A panalphabetic window is a substring containing all letters of an alphabet in the right order.
# e.g.
# Input string = "AxxxxxxBxxxxCxxxADxBCxD"
# Alphabet = [A, B, C, D]
# Windows = ["AxxxxxxBxxxxCxxxAD", "ADxBCxD"]
# Return shortest = "ADxBCxD"

def shortest_panalphabetic_window(alphabet, string):
    
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
        
        
        

