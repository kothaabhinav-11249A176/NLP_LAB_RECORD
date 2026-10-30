# Backoff Activity 3: Calculate percentage resolved at each level
from collections import Counter

text = "i am learning nlp i am learning python"
tokens = text.lower().split()
uni = Counter(tokens)
bi = Counter(zip(tokens, tokens[1:]))
tri = Counter(zip(tokens, tokens[1:], tokens[2:]))
N = len(tokens)
alpha = 0.4

test_triples = [("i", "am", "learning"),
                ("learning", "i", "am"),
                ("is", "fun", "python")]
levels = {"trigram": 0, "bigram": 0, "unigram": 0}

def stupid_backoff(w1, w2, w3):
    if tri[(w1, w2, w3)] > 0:
        return tri[(w1, w2, w3)] / bi[(w1, w2)], "trigram"
    elif bi[(w2, w3)] > 0:
        return alpha * bi[(w2, w3)] / uni[w2], "bigram"
    return alpha ** 2 * uni[w3] / N, "unigram"

for triple in test_triples:
    p, level = stupid_backoff(*triple)
    levels[level] += 1
    print(f"{triple} -> {level}, score = {p:.5f}")

total = len(test_triples)
print("\nPercentage at each level:")
for level, count in levels.items():
    percentage = count / total * 100
    print(f"{level}: {percentage:.2f}%")
