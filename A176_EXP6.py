import re
from collections import Counter
text = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
words = re.findall(r"[a-z']+", text.lower())
unigram = Counter(words)
bigram = Counter(zip(words, words[1:]))
V = len(unigram)
def probability(w1, w2, k):
    return (bigram[(w1, w2)] + k) / (unigram[w1] + k * V)
sentence = "the fox runs"
test = sentence.split()
for k in [0.1, 0.5, 1]:
    p = 1
    for i in range(len(test) - 1):
        p *= probability(test[i], test[i + 1], k)
    print("k =", k, "Sentence Probability =", round(p, 8))