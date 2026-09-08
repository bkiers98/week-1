

# add code below ...
def palindrome(word):
    '''
        This function receives a string and returns True or False to 
        indicate whether or not it is a palindrome.
    '''

    punctuation = '.,?! '
    for char in punctuation:
        word = word.replace(char, "")
    word = word.lower()
    for letter in range(len(word)):
        if word[letter] != word[-(letter + 1)]:
            return False
    return True

def parentheses(sequence):
    '''
        This function takes a string and returns True or False depending on 
        if the string's parentheses are balanced.
    '''

    open_count = 0


    for char in sequence:
        if char == '(':
            open_count += 1
        elif char == ')':
            if open_count == 0:
                return False
            else:
                open_count -= 1

    if open_count == 0:
        return True
    else:
        return False