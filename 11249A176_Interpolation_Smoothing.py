# Experiment 3: Linear Interpolation (Unigram + Bigram + Trigram)
from collections import Counter

text = "i am learning nlp i am learning python"
tokens = text.lower().split()
unigram_freq = Counter(tokens)
bigram_freq = Counter(zip(tokens, tokens[1:]))
trigram_freq = Counter(zip(tokens, tokens[1:], tokens[2:]))
N = len(tokens)

# Interpolation weights must sum to 1
lambda1, lambda2, lambda3 = 0.1, 0.3, 0.6

def interpolated_prob(w1, w2, w3):
    p_uni = unigram_freq[w3] / N
    p_bi = (bigram_freq[(w2, w3)] / unigram_freq[w2]
            if unigram_freq[w2] > 0 else 0)
    p_tri = (trigram_freq[(w1, w2, w3)] / bigram_freq[(w1, w2)]
             if bigram_freq[(w1, w2)] > 0 else 0)
    return lambda1 * p_uni + lambda2 * p_bi + lambda3 * p_tri

test_triples = [
    ("i", "am", "learning"),
    ("am", "learning", "nlp"),
    ("is", "fun", "to")
]

print(f"lambda1={lambda1}, lambda2={lambda2}, lambda3={lambda3}\n")
for w1, w2, w3 in test_triples:
    p = interpolated_prob(w1, w2, w3)
    print(f"P({w3}|{w1},{w2}) [Interpolation] = {p:.5f}")
