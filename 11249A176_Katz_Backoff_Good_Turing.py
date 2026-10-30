# Backoff Activity 4: Simplified Katz Backoff with Good-Turing discounting
from collections import Counter

text = "i am learning nlp i am learning python"
tokens = text.lower().split()
uni = Counter(tokens)
bi = Counter(zip(tokens, tokens[1:]))
tri = Counter(zip(tokens, tokens[1:], tokens[2:]))
N = len(tokens)
alpha = 0.4

def good_turing_count(count, frequency):
    """Return a Good-Turing adjusted count when the required counts exist."""
    if count == 0:
        return 0
    Nr = sum(1 for value in frequency.values() if value == count)
    Nr1 = sum(1 for value in frequency.values() if value == count + 1)
    if Nr > 0 and Nr1 > 0:
        return (count + 1) * Nr1 / Nr
    return count

def stupid_backoff(w1, w2, w3):
    if tri[(w1, w2, w3)] > 0:
        return tri[(w1, w2, w3)] / bi[(w1, w2)]
    if bi[(w2, w3)] > 0:
        return alpha * bi[(w2, w3)] / uni[w2]
    return alpha ** 2 * uni[w3] / N

def katz_style_backoff(w1, w2, w3):
    tri_count = tri[(w1, w2, w3)]
    if tri_count > 0:
        adjusted = good_turing_count(tri_count, tri)
        return adjusted / bi[(w1, w2)]

    bi_count = bi[(w2, w3)]
    if bi_count > 0:
        adjusted = good_turing_count(bi_count, bi)
        return alpha * adjusted / uni[w2]

    uni_count = uni[w3]
    if uni_count > 0:
        adjusted = good_turing_count(uni_count, uni)
        return alpha ** 2 * adjusted / N
    return 0.0

test_triples = [("i", "am", "learning"),
                ("learning", "i", "am"),
                ("is", "fun", "python")]

print(f"{'Test trigram':<30}{'Stupid Backoff':<18}{'Katz-style'}")
for triple in test_triples:
    stupid = stupid_backoff(*triple)
    katz = katz_style_backoff(*triple)
    print(f"{str(triple):<30}{stupid:<18.5f}{katz:.5f}")
