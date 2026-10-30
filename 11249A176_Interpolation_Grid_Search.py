# Interpolation Activity 4: Grid search for best interpolation weights
from collections import Counter
import math

text = "i am learning nlp i am learning python"
tokens = text.lower().split()
uni = Counter(tokens)
bi = Counter(zip(tokens, tokens[1:]))
tri = Counter(zip(tokens, tokens[1:], tokens[2:]))
N = len(tokens)

heldout = [("i", "am", "learning"), ("am", "learning", "nlp")]

def components(w1, w2, w3):
    p_uni = uni[w3] / N
    p_bi = bi[(w2, w3)] / uni[w2] if uni[w2] else 0
    p_tri = tri[(w1, w2, w3)] / bi[(w1, w2)] if bi[(w1, w2)] else 0
    return p_uni, p_bi, p_tri

def sentence_log_probability(l1, l2, l3):
    total = 0.0
    for triple in heldout:
        p_uni, p_bi, p_tri = components(*triple)
        p = l1 * p_uni + l2 * p_bi + l3 * p_tri
        if p <= 0:
            return float("-inf")
        total += math.log(p)
    return total

best_score = float("-inf")
best_weights = None

# Search weights in increments of 0.1; their sum is 1.
for i in range(11):
    for j in range(11 - i):
        m = 10 - i - j
        l1, l2, l3 = i / 10, j / 10, m / 10
        score = sentence_log_probability(l1, l2, l3)
        if score > best_score:
            best_score = score
            best_weights = (l1, l2, l3)

print("Held-out sentence: i am learning nlp")
print("Best weights (lambda1, lambda2, lambda3):", best_weights)
print(f"Maximum log probability = {best_score:.5f}")
print(f"Sentence probability = {math.exp(best_score):.5f}")
