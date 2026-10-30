# Add-k Activity 4: Discuss the effect of k
from collections import Counter

text = "i am learning nlp i am learning python"
tokens = text.lower().split()
unigram_freq = Counter(tokens)
bigram_freq = Counter(zip(tokens, tokens[1:]))
V = len(unigram_freq)

def addk_prob(w1, w2, k):
    return (bigram_freq[(w1, w2)] + k) / (unigram_freq[w1] + k * V)

test_pairs = [("i", "am"), ("i", "python")]
k_values = [0.0001, 0.01, 0.1, 0.5, 1.0]

print("Effect of k on bigram probabilities\n")
for w1, w2 in test_pairs:
    print(f"Bigram: ({w1}, {w2})")
    for k in k_values:
        print(f"k = {k:<6} Probability = {addk_prob(w1, w2, k):.5f}")
    print()

print("DISCUSSION")
print("As k approaches 0, Add-k approaches MLE for seen bigrams.")
print("Unseen bigrams approach probability 0.")
print("At k = 1, Add-k becomes Add-1 (Laplace) smoothing.")
