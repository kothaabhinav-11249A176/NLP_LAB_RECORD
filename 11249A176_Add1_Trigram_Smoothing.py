# Activity 5: Add-1 smoothing for a trigram model
from collections import Counter

text = "I like Python " * 16
tokens = text.lower().split()
unigram_freq = Counter(tokens)
bigram_freq = Counter(zip(tokens, tokens[1:]))
trigram_freq = Counter(zip(tokens, tokens[1:], tokens[2:]))
V = len(unigram_freq)

def add1_trigram(w1, w2, w3):
    numerator = trigram_freq[(w1, w2, w3)] + 1
    denominator = bigram_freq[(w1, w2)] + V
    return numerator / denominator

test_triples = [
    ("i", "like", "python"),
    ("like", "python", "i"),
    ("python", "python", "python")
]

print("Vocabulary size V =", V)
for w1, w2, w3 in test_triples:
    print(f"P({w3}|{w1},{w2}) = {add1_trigram(w1, w2, w3):.5f}")
