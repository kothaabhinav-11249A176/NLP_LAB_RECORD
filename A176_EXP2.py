import re
from collections import Counter
text = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
unigram = Counter()
bigram = Counter()
for line in text.split("\n"):
    words = ["<s>"] + re.findall(r"[a-z']+", line.lower()) + ["</s>"]
    for i in range(len(words) - 1):
        unigram[words[i]] += 1
        bigram[(words[i], words[i + 1])] += 1
print("BIGRAM PROBABILITY TABLE")
print("-" * 50)
print(f"{'Current Word':<15}{'Next Word':<15}{'Probability':<10}")
print("-" * 50)
for (w1, w2), count in bigram.items():
    probability = count / unigram[w1]
    print(f"{w1:<15}{w2:<15}{probability:.3f}")