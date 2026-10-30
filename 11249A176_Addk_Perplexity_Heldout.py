# Add-k Activity 3: Calculate perplexity on a held-out test set
from collections import Counter
import math

train_text = (
    "i like python i enjoy coding "
    "i like coding i enjoy python "
    "i like python i enjoy coding"
)
test_text = "i like coding"

train_tokens = train_text.lower().split()
test_tokens = test_text.lower().split()
unigram_freq = Counter(train_tokens)
bigram_freq = Counter(zip(train_tokens, train_tokens[1:]))
V = len(unigram_freq)
N = len(test_tokens) - 1

k_values = [0.01, 0.1, 0.5, 1.0]

def addk_prob(w1, w2, k):
    return (bigram_freq[(w1, w2)] + k) / (unigram_freq[w1] + k * V)

def calculate_perplexity(k):
    log_probability = 0.0
    for i in range(1, len(test_tokens)):
        w1, w2 = test_tokens[i - 1], test_tokens[i]
        log_probability += math.log(addk_prob(w1, w2, k))
    return math.exp(-log_probability / N)

print("Held-out text:", test_text)
results = {}
for k in k_values:
    perplexity = calculate_perplexity(k)
    results[k] = perplexity
    print(f"k = {k:<5} Perplexity = {perplexity:.5f}")

best_k = min(results, key=results.get)
print(f"\nBest k = {best_k}")
print(f"Minimum perplexity = {results[best_k]:.5f}")
