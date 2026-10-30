# Interpolation Activity 1: Calculate probabilities using given weights
from collections import Counter

text = "i am learning nlp i am learning python"
tokens = text.lower().split()
uni = Counter(tokens)
bi = Counter(zip(tokens, tokens[1:]))
tri = Counter(zip(tokens, tokens[1:], tokens[2:]))
N = len(tokens)
lambda1, lambda2, lambda3 = 0.1, 0.3, 0.6

def interpolated_prob(w1, w2, w3):
    p_uni = uni[w3] / N
    p_bi = bi[(w2, w3)] / uni[w2] if uni[w2] else 0
    p_tri = tri[(w1, w2, w3)] / bi[(w1, w2)] if bi[(w1, w2)] else 0
    return lambda1 * p_uni + lambda2 * p_bi + lambda3 * p_tri

test_triples = [("i", "am", "learning"),
                ("am", "learning", "nlp"),
                ("is", "fun", "to")]

print("Weights:", lambda1, lambda2, lambda3)
for triple in test_triples:
    print(f"P({triple[2]}|{triple[0]},{triple[1]}) = {interpolated_prob(*triple):.5f}")
