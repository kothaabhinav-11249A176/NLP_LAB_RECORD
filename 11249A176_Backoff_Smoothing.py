# Experiment 4: Stupid Backoff Smoothing (alpha = 0.4)
from collections import Counter

text = "i am learning nlp i am learning python"
tokens = text.lower().split()
unigram_freq = Counter(tokens)
bigram_freq = Counter(zip(tokens, tokens[1:]))
trigram_freq = Counter(zip(tokens, tokens[1:], tokens[2:]))
N = len(tokens)
alpha = 0.4

def stupid_backoff(w1, w2, w3):
    if trigram_freq[(w1, w2, w3)] > 0:
        return trigram_freq[(w1, w2, w3)] / bigram_freq[(w1, w2)]
    elif bigram_freq[(w2, w3)] > 0:
        return alpha * bigram_freq[(w2, w3)] / unigram_freq[w2]
    else:
        return (alpha ** 2) * unigram_freq[w3] / N

test_triples = [
    ("i", "am", "learning"),
    ("am", "learning", "nlp"),
    ("is", "fun", "to")
]

print(f"Alpha = {alpha}\n")
for w1, w2, w3 in test_triples:
    p = stupid_backoff(w1, w2, w3)
    if trigram_freq[(w1, w2, w3)] > 0:
        level = "trigram"
    elif bigram_freq[(w2, w3)] > 0:
        level = "bigram"
    else:
        level = "unigram"
    print(f"P({w3}|{w1},{w2}) [Backoff -> {level}] = {p:.5f}")
