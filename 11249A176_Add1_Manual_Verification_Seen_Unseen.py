# Activity 3: Manually verify one seen and one unseen bigram
from collections import Counter

text = "I like Python " * 16
tokens = text.lower().split()
unigram_freq = Counter(tokens)
bigram_freq = Counter(zip(tokens, tokens[1:]))
V = len(unigram_freq)

def add1_prob(w1, w2):
    return (bigram_freq[(w1, w2)] + 1) / (unigram_freq[w1] + V)

# Seen bigram
w1, w2 = "i", "like"
print("Seen bigram (i, like)")
print("Count =", bigram_freq[(w1, w2)])
print("Manual probability = (16 + 1) / (16 + 3)")
print("Program probability =", round(add1_prob(w1, w2), 5))

# Unseen bigram
w1, w2 = "python", "python"
print("\nUnseen bigram (python, python)")
print("Count =", bigram_freq[(w1, w2)])
print("Manual probability = (0 + 1) / (16 + 3)")
print("Program probability =", round(add1_prob(w1, w2), 5))
