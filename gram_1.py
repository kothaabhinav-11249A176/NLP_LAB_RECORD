
from collections import Counter

sentences = [
    ["I", "love", "NLP"],
    ["I", "love", "deep", "learning"],
    ["I", "study", "NLP"],
    ["You", "love", "NLP"]
]

bigrams = Counter()
for s in sentences:
    words = ["<s>"] + s + ["</s>"]
    for i in range(len(words) - 1):
        bigrams[(words[i], words[i+1])] += 1

print("I love:", bigrams[("I", "love")])
print("I study:", bigrams[("I", "study")])
print("love NLP:", bigrams[("love", "NLP")])
print("love deep:", bigrams[("love", "deep")])

p = (3/4) * (2/3) * (2/3) * 1
print("Sentence probability:", round(p, 3))