# Interpolation Activity 2: Compare two sets of weights
from collections import Counter

text = "i am learning nlp i am learning python"
tokens = text.lower().split()
uni = Counter(tokens)
bi = Counter(zip(tokens, tokens[1:]))
tri = Counter(zip(tokens, tokens[1:], tokens[2:]))
N = len(tokens)

test_triples = [("i", "am", "learning"),
                ("am", "learning", "nlp"),
                ("is", "fun", "to")]

def interpolate(w1, w2, w3, l1, l2, l3):
    p_uni = uni[w3] / N
    p_bi = bi[(w2, w3)] / uni[w2] if uni[w2] else 0
    p_tri = tri[(w1, w2, w3)] / bi[(w1, w2)] if bi[(w1, w2)] else 0
    return l1 * p_uni + l2 * p_bi + l3 * p_tri

weight_sets = [(0.1, 0.3, 0.6), (0.6, 0.3, 0.1)]
for weights in weight_sets:
    print(f"\nWeights: {weights}")
    for triple in test_triples:
        p = interpolate(*triple, *weights)
        print(f"P({triple[2]}|{triple[0]},{triple[1]}) = {p:.5f}")
