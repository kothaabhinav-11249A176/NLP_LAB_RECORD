# Experiment 2: Add-k Smoothing for Bigram Model
from collections import Counter

text = "i am learning nlp i am learning python"
tokens = text.lower().split()
unigram_freq = Counter(tokens)
bigram_freq = Counter(zip(tokens, tokens[1:]))
vocab_size = len(unigram_freq)

test_pairs = [
    ("i", "am"),
    ("am", "learning"),
    ("learning", "nlp"),
    ("natural", "language")
]

def addk_prob(w1, w2, k):
    """Calculate P(w2 | w1) using Add-k smoothing."""
    numerator = bigram_freq[(w1, w2)] + k
    denominator = unigram_freq[w1] + k * vocab_size
    return numerator / denominator

k_values = [0.01, 0.1, 0.5, 1.0]
print(f"{'Bigram':<25}", end="")
for k in k_values:
    print(f"{('k=' + str(k)):<12}", end="")
print()

for w1, w2 in test_pairs:
    print(f"{str((w1, w2)):<25}", end="")
    for k in k_values:
        print(f"{addk_prob(w1, w2, k):<12.5f}", end="")
    print()
