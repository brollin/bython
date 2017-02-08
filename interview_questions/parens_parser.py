# v1: Imagine that we're given a string containing a snippet of code
# we want to validate that all the parentheses (if any) in that snippet are
# properly matched
# GOOD
# "()" 
# "()()"
# "(())"
# "(())()"
# "for(int i=0; i<5; i++) { echo 'hi' };"
# BAD
# "("
# ")"
# ")("
# "(()))"
# "((())"

# v2: Generally there's a user somewhere that needs to be able to fix
# code that's rejected by the parser. So, let's provide that user with some
# feedback about *where* the failure occurred.
# "()(()"

# v3: Return a helpful string in addition to the index

def validate_paren(code):
    if not code:
        return True
    
    open_parens = []
    for index, char in enumerate(code):
        if char == "(":
            open_parens.append(index)
        elif char == ")":
            if open_parens:
                open_parens.pop()
            else:
                return ("Error: Extra closing parentheses found at index %s" % index, index)

    if open_parens:
        return ("Error: Unclosed parentheses found at index %s" % open_parens[-1], open_parens[-1])
    
    return True


assert validate_paren( "()" ) == True
assert validate_paren("()()") == True
assert validate_paren("(())")  == True
assert validate_paren("(())()")  == True
assert validate_paren("for(int i=0; i<5; i++) { echo 'hi' };")  == True
# BAD
assert validate_paren("(") == 0
assert validate_paren(")") == 0
assert validate_paren(")(") == 0
assert validate_paren("(()))") == 4
assert validate_paren("((())") == 0
