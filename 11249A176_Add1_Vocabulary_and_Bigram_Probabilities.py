# Activity 1: Find vocabulary size and calculate Add-1 probabilities
from collections import Counter

text = "i am learning nlp i am learning python"
tokens = text.lower().split()
unigram_freq = Counter(tokens)
bigram_freq = Counter(zip(tokens, tokens[1:]))
V = len(unigram_freq)

print("Vocabulary size V =", V)
test_pairs = [("i", "am"), ("am", "learning"),
              ("learning", "nlp"), ("natural", "language")]

for w1, w2 in test_pairs:
    numerator = bigram_freq[(w1, w2)] + 1
    denominator = unigram_freq[w1] + V
    probability = numerator / denominator
    print(f"P({w2}|{w1}) = {probability:.5f}")
