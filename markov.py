"""Generate Markov text from text files."""

import random
import sys

file_name = sys.argv[1]

def open_and_read_file(file_path):
    """Take file path as string; return text as string.
    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open(file_name)
    text = file.read()
    return text



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.
    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
    For example:
        >>> chains = make_chains('hi there mary hi there juanita')
    Each bigram (except the last) will be a key in chains:
        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]
    Each item in chains is a list of all possible following words:
        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        >>> chains[('there','juanita')]
        [None]
        
        {Would, you} : [could, could, could, like, like]
    """
    full_text = open_and_read_file(file_name)
    full_text_lst = full_text.rstrip('\n').split()
    
    chains = {}

    for i in range(len(full_text_lst) - 2):
        # the next 3 lines will create a empty list and then appends the word at i(would) & i+1(you)
        key_list = []
        key_list.append(full_text_lst[i])
        key_list.append(full_text_lst[i + 1])

        key_tuple = tuple(key_list) #takes the key_list and convers it to a tuple {would, you}

        
        if key_tuple in chains.keys():
            chains.get(key_tuple).append(full_text_lst[i + 2])
        else:
            chains[key_tuple] = [full_text_lst[i + 2]]
            
                

    # for k, v in chains.items():
    #     print(f"{k}: {v})")

    # your code goes here

    return chains


def make_text(chains):
    """Return text from chains."""

    #Set variable words to empty list to store Markov chain of text
    words = []

    #Set variable chains to dict called from make_chains function
    chains = make_chains(file_name)

    #Set variable keys to keys in dict
    keys = chains.keys()

    #Set variable first_key to a random tuple from keys
    first_key = random.choice(list(keys))

    #First word of next tuple is the second item in the first_key tuple
    first_word = first_key[1]

    #First next word is a random word from the list of values stored at
    #first_key in dict
    first_next = random.choice(list(chains[first_key]))

    #Add first item in first_key to words capitalized
    words.append(first_key[0].capitalize())

    #Add second item in first_key to words
    words.append(first_key[1])

    #Add first next word to words
    words.append(first_next)

    #Create a condition that is always true
    while len(words) > 0:

        #List of the current key
        #Item at index 0 is the second to last word in list
        #Item at index 1 is the last word in list
        current_key_list = []
        current_key_list.append(words[-2])
        current_key_list.append(words[-1])

        #Create a tuple from the list of current key
        current_key = tuple(current_key_list)

        #If current_key not in keys, break the loop
        if current_key not in keys:
            break

        #If current_key in keys, continue adding to list of words
        else:

            #Choose a random word from the list of words stored
            #as the value for the current key
            current_next = random.choice(list(chains[current_key]))

            #Add new random word to list of words
            words.append(current_next)

    #Return joined list of words
    return " ".join(words)
    

    # your code goes here

    # while tuple in keys:

    # next_key = key[1] + next_word

    # next_word = random.choice(chains[key])

    # return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)