from collections import Counter
import re
from string import ascii_lowercase

def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('big.txt').read()))

# Number of total words in file
sum_words = sum(WORDS.values())
# Number of distinct words
num_words = len(WORDS)

def bigtxt_word_exists(word): return WORDS[word] > 0

# Returns probability of a word appearing
def prob(word): return WORDS[word] * 1.0 / sum_words

def tuplify(word):
    return [(word[0:x], word[x:len(word)]) for x in range(len(word)+1)]

def operate(p, f, l, word):
    result = []
    for t in tuplify(word):
        for c in l:
            if p(t, c):
                val = f(t, c)
                if bigtxt_word_exists(val): result.append(f(t, c))
    return result

def insert_edits(word):
    return operate(lambda t, c: True, lambda t, c: t[0] + c + t[1], ascii_lowercase, word)

def remove_edits(word):
    return operate(lambda t, c: t[0], lambda t, c: t[0][0:len(t[0])-1] + t[1], [""], word)

def change_edits(word):
    return operate(lambda t, c: t[1], lambda t, c: t[0] + c + t[1][1:len(t[1])], ascii_lowercase, word)
    
def edits(word):
    return insert_edits(word) + remove_edits(word) + change_edits(word)

def corrections(word):
    if WORDS[word] > 0: return []
    return sorted(edits(word), key=prob, reverse=True)

def main():
    input_words = raw_input("Enter text: ").split(" ")
    for word in input_words:
        print(word + " => [" + ", ".join(corrections(word)) + "]")

main()
