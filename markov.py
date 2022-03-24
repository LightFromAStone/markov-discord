"""Generate Markov text from text files."""

from random import choice
# from pprint import pprint

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path, 'rt') as input_file:
        read_data = input_file.read() # NOTE this has no restrictions on the input size. It could try to read in a file larger than system memory. Although, this scenario is unlikely

    return read_data.rstrip()


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
    """

    chains = {}

    words = text_string.split()
    # Create tuples for each bigram and add it as a key to our dictionary. Append the word after the bigram to the list of words for that bigram key
    for i in range(len(words) - 2):
        if (words[i], words[i + 1]) not in chains:
            chains[(words[i], words[i + 1])] = []
        chains[(words[i], words[i + 1])].append(words[i + 2])

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    link = choice(list(chains))
    words.append(link[0].capitalize())
    words.append(link[1])
    
    while link in chains:
        next_word = choice(chains[link])
        words.append(next_word)
        link = (link[1], next_word)

    return ' '.join(words)


# input_path = 'green-eggs.txt'
input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
# pprint(chains)

# Produce random text
random_text = make_text(chains)

print(random_text)
