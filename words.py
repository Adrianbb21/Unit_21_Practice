def print_upper_words(words):
    """Prints each word on a seperate line, and converts them into uppercase"""
    for word in words:
        print(word.upper())

def print_e_words(words):
    """Print each word on a seperate line, uppercased but only if they start with E or e"""
    for word in words:
        if word.startwith('e') or word.startswith('E'):
            print(word.upper())

def print_specific_words(words, must_start_with):
    """ Prints each wor on a seperate line, uppercased, if it starts with one of the given"""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())