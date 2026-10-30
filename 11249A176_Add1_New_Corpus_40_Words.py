# Activity 2: Add-1 probabilities for a new corpus (at least 40 words)
import re
from collections import Counter

# Repeated sentence creates a corpus with more than 40 word tokens.
text = "I like Python. " * 16
tokens = re.findall(r"\b[a-z]+\b", text.lower())

unigram_freq = Counter(tokens)
bigram_freq = Counter(zip(tokens, tokens[1:]))
V = len(unigram_freq)

print("Total words =", len(tokens))
print("Vocabulary size V =", V)

test_pairs = [("i", "like"), ("like", "python"), ("python", "python")]
for w1, w2 in test_pairs:
    numerator = bigram_freq[(w1, w2)] + 1
    denominator = unigram_freq[w1] + V
    probability = numerator / denominator
    print(f"P({w2}|{w1}) = {probability:.5f}")
