

# add code below ...
def palindrome(word):
    '''
        This function receives a string and returns True or False to indicate whether or not it is a palindrome.
    '''

    punctuation = '.,?! '
    for char in punctuation:
        word = word.replace(char, "")
    word = word.lower()
    for letter in range(len(word)):
        if word[letter] != word[-(letter + 1)]:
            return False
    return True

