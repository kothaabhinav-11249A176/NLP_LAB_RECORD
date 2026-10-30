# Interpolation Activity 3: Display individual MLE components
from collections import Counter

text = "i am learning nlp i am learning python"
tokens = text.lower().split()
uni = Counter(tokens)
bi = Counter(zip(tokens, tokens[1:]))
tri = Counter(zip(tokens, tokens[1:], tokens[2:]))
N = len(tokens)
l1, l2, l3 = 0.1, 0.3, 0.6

test_triples = [("i", "am", "learning"),
                ("am", "learning", "nlp"),
                ("is", "fun", "to")]

def show_components(w1, w2, w3):
    p_uni = uni[w3] / N
    p_bi = bi[(w2, w3)] / uni[w2] if uni[w2] > 0 else 0
    p_tri = tri[(w1, w2, w3)] / bi[(w1, w2)] if bi[(w1, w2)] > 0 else 0
    final_p = l1 * p_uni + l2 * p_bi + l3 * p_tri
    print(f"\nTriple: ({w1}, {w2}, {w3})")
    print(f"Unigram MLE = {p_uni:.5f}")
    print(f"Bigram MLE = {p_bi:.5f}")
    print(f"Trigram MLE = {p_tri:.5f}")
    print(f"Interpolated probability = {final_p:.5f}")

print("Weights:", l1, l2, l3)
for triple in test_triples:
    show_components(*triple)
