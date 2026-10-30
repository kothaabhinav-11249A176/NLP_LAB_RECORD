# Add-k Activity 2: Plot probabilities as k increases
from collections import Counter
import matplotlib.pyplot as plt

text = "i am learning nlp i am learning python"
tokens = text.lower().split()
unigram_freq = Counter(tokens)
bigram_freq = Counter(zip(tokens, tokens[1:]))
V = len(unigram_freq)

def addk_prob(w1, w2, k):
    return (bigram_freq[(w1, w2)] + k) / (unigram_freq[w1] + k * V)

k_values = [0.01, 0.05, 0.1, 0.2, 0.3, 0.4,
            0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

seen_probs = [addk_prob("i", "am", k) for k in k_values]
unseen_probs = [addk_prob("i", "python", k) for k in k_values]

plt.plot(k_values, seen_probs, marker="o", label="Seen: (i, am)")
plt.plot(k_values, unseen_probs, marker="s", label="Unseen: (i, python)")
plt.xlabel("Smoothing parameter k")
plt.ylabel("P(w2 | w1)")
plt.title("Add-k Smoothing: Probability vs k")
plt.legend()
plt.grid(True)
plt.show()
