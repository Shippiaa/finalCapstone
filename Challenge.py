def add_prefix_un(word):
    """
    Adds the prefix 'un' to the beginning of the given word. Checks if the input is a string.
    
    Parameters:
    - word: The word to which the prefix will be added. Should be a string.
    
    Returns:
    - The new word with 'un' prefix added. If input is not a string, returns None.
    """
    if not isinstance(word, str):
        print("Error: The word should be a string.")
        return None
    new_word = 'un' + word
    print(new_word)
    return new_word

def make_word_groups(vocab_words):
    """
    Creates new words with a common prefix given a list of vocabulary words, ensuring all inputs are strings.
    
    Parameters:
    - vocab_words: A list where the first element is the prefix and the remaining elements are words to be prefixed.
    
    Returns:
    - A list of new words with the common prefix. If the input is not a list of strings, returns None.
    """
    if not isinstance(vocab_words, list) or not all(isinstance(word, str) for word in vocab_words):
        print("Error: Input must be a list of strings.")
        return None
    prefix = vocab_words[0]
    new_list = [prefix]
    for word in vocab_words[1:]:
        new_word = prefix + word
        new_list.append(new_word)
    print(new_list)
    return new_list


def remove_suffix_ness(word):
    """
    Removes the suffix 'ness' from a word and applies necessary adjustments.
    
    Parameters:
    - word (str): The word from which 'ness' suffix will be removed.
    
    Returns:
    - str: The word after removal of 'ness' and necessary adjustments.
    """
    if word.endswith('ness'):
        base_word = word[:-4]
        if base_word[-1] == 'i':
            new_word = base_word[:-1] + 'y'
        else:
            new_word = base_word
        print(new_word)
        return new_word
    print(word)
    return word

def adjective_to_verb(sentence, index):
    """
    Changes an adjective from a given sentence into a verb. This function
    handles some edge cases with a simple mapping for known exceptions.
    
    Parameters:
    - sentence (str): The sentence containing the adjective.
    - index (int): The index of the word in the sentence to be transformed.
    
    Returns:
    - str: The verb form of the given adjective.
    """
    # Mapping for known exceptions
    exceptions = {
        "whole": "encompass",
        "true": "truthen",
    }
    
    words = sentence.split()
    adjective = words[index].strip('.,!?')
    
    # Check for exceptions
    if adjective in exceptions:
        verb = exceptions[adjective]
    elif adjective[-1] == 'e':
        verb = adjective + 'n'
    else:
        verb = adjective + 'en'
    
    print(verb)
    return verb

# Example usages with the improved functions
add_prefix_un("happy") 
add_prefix_un("manageable")     
make_word_groups(['en', 'close', 'joy', 'lighten'])
remove_suffix_ness("heaviness")
remove_suffix_ness("sadness")
adjective_to_verb("I need to make that whole.", -1)


