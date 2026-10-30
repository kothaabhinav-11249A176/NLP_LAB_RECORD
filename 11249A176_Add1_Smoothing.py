# Experiment 1: Add-1 (Laplace) Smoothing for Bigram Model
from collections import Counter

text = "i am learning nlp i am learning python"
tokens = text.lower().split()

unigram_freq = Counter(tokens)
bigram_freq = Counter(zip(tokens, tokens[1:]))
vocab_size = len(unigram_freq)

def add1_prob(w1, w2):
    numerator = bigram_freq[(w1, w2)] + 1
    denominator = unigram_freq[w1] + vocab_size
    return numerator / denominator

test_pairs = [
    ("i", "am"),
    ("am", "learning"),
    ("learning", "nlp"),
    ("natural", "language")
]

print(f"Vocabulary size (V) = {vocab_size}\n")
print(f"{'Bigram':<25}{'Count':<8}{'P(w2|w1) Add-1':<15}")
for w1, w2 in test_pairs:
    p = add1_prob(w1, w2)
    count = bigram_freq[(w1, w2)]
    print(f"{str((w1, w2)):<25}{count:<8}{p:<15.4f}")
