from collections import Counter
import re
from string import ascii_lowercase

def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('big.txt').read()))

# Number of total words in file
sum_words = sum(WORDS.values())
# Number of distinct words
num_words = len(WORDS)

# Returns probability of a word appearing
def prob(word): return WORDS[word] / sum_words

def insert_edits(word):
    word_len = len(word)
    result = []
    for x in range(0, word_len + 1):
        prefix = word[0:x]
        suffix = word[x:word_len]
        for y in range(0, 26):
            char = chr(97 + y)
            result.append(prefix + char + suffix)
    return result

def remove_edits(word):
    result = []
    word_len = len(word)
    for x in range(0, word_len):
        prefix = word[0:x]
        suffix = word[x + 1:word_len]
        result.append(prefix + suffix)
    return result

def change_edits(word):
    result = []
    word_len = len(word)
    for x in range(0, word_len):
        prefix = word[0:x]
        suffix = word[x + 1:word_len]
        for y in range(0, 26):
            char = chr(97 + y)
            result.append(prefix + char + suffix)
    return result

def edits(word):
    edits = insert_edits(word)
    edits.extend(remove_edits(word))
    edits.extend(change_edits(word))
    return edits
