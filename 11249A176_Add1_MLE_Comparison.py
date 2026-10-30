# Activity 4: Compare raw MLE probability with Add-1 smoothing
from collections import Counter

text = "I like Python " * 16
tokens = text.lower().split()
unigram_freq = Counter(tokens)
bigram_freq = Counter(zip(tokens, tokens[1:]))
V = len(unigram_freq)

w1, w2 = "i", "like"
count = bigram_freq[(w1, w2)]
context_count = unigram_freq[w1]

mle_prob = count / context_count
add1_prob = (count + 1) / (context_count + V)

print("Bigram =", (w1, w2))
print(f"Raw MLE probability = {mle_prob:.5f}")
print(f"Add-1 probability = {add1_prob:.5f}")
print(f"Probability reduction = {mle_prob - add1_prob:.5f}")
