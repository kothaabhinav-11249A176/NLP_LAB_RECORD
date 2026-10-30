# Add-k Activity 1: Tabulate probabilities for different k values
from collections import Counter

text = "i am learning nlp i am learning python"
tokens = text.lower().split()
unigram_freq = Counter(tokens)
bigram_freq = Counter(zip(tokens, tokens[1:]))
V = len(unigram_freq)

k_values = [0.01, 0.1, 0.5, 1.0]
test_pairs = [("i", "am"), ("am", "learning"),
              ("learning", "nlp"), ("natural", "language")]

def addk_prob(w1, w2, k):
    return (bigram_freq[(w1, w2)] + k) / (unigram_freq[w1] + k * V)

print(f"{'Bigram':<22}", end="")
for k in k_values:
    print(f"{('k=' + str(k)):<12}", end="")
print()

for w1, w2 in test_pairs:
    print(f"{w1 + ' -> ' + w2:<22}", end="")
    for k in k_values:
        print(f"{addk_prob(w1, w2, k):<12.5f}", end="")
    print()
