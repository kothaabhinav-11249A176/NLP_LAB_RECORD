import re
from collections import defaultdict, Counter
text = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
bigram = defaultdict(Counter)
trigram = defaultdict(Counter)
for line in text.split("\n"):
    words = re.findall(r"[a-z']+", line.lower())
    w = ["<s>"] + words + ["</s>"]
    for i in range(len(w) - 1):
        bigram[w[i]][w[i + 1]] += 1
    w = ["<s>", "<s>"] + words + ["</s>"]
    for i in range(len(w) - 2):
        trigram[(w[i], w[i + 1])][w[i + 2]] += 1
word = "<s>"
bigram_sentence = []
for i in range(15):
    if word not in bigram:
        break
    word = bigram[word].most_common(1)[0][0]
    if word == "</s>":
        break
    bigram_sentence.append(word)
w1 = "<s>"
w2 = "<s>"
trigram_sentence = []
for i in range(15):
    if (w1, w2) not in trigram:
        break
    w3 = trigram[(w1, w2)].most_common(1) [0][0]
    if w3 == "</s>":
        break
    trigram_sentence.append(w3)
    w1 = w2
    w2 = w3
print("BIGRAM  :", " ".join(bigram_sentence))
print("TRIGRAM :", " ".join(trigram_sentence))