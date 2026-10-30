# Backoff Activity 2: Compare alpha = 0.4 and alpha = 0.7
from collections import Counter

text = "i am learning nlp i am learning python"
tokens = text.lower().split()
uni = Counter(tokens)
bi = Counter(zip(tokens, tokens[1:]))
tri = Counter(zip(tokens, tokens[1:], tokens[2:]))

# The trigram is missing, but the bigram (i, am) exists.
w1, w2, w3 = "learning", "i", "am"
bigram_probability = bi[(w2, w3)] / uni[w2]

print("Test trigram:", (w1, w2, w3))
print(f"Bigram MLE = {bigram_probability:.5f}")
for alpha in [0.4, 0.7]:
    score = alpha * bigram_probability
    print(f"Alpha = {alpha}: Backoff score = {score:.5f}")
