import re
from collections import Counter
text = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
trigram = Counter()
quadgram = Counter()
for line in text.split("\n"):
    words = ["<s>", "<s>", "<s>"] + \
            re.findall(r"[a-z']+", line.lower()) + ["</s>"]
    for i in range(len(words) - 3):
        trigram[(words[i], words[i+1], words[i+2])] += 1
        quadgram[(words[i], words[i+1],
                  words[i+2], words[i+3])] += 1
print("4-GRAM PROBABILITY TABLE")
print("-" * 65)
print(f"{'Previous 3 Words':<35}{'Next Word':<15}{'Probability'}")
print("-" * 65)
for (w1, w2, w3, w4), count in quadgram.items():
    probability = count / trigram[(w1, w2, w3)]
    previous = w1 + " " + w2 + " " + w3
    print(f"{previous:<35}{w4:<15}{probability:.3f}")