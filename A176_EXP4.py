import nltk
import re
from nltk.corpus import gutenberg
from collections import Counter
nltk.download("gutenberg")
print("Loading corpus...")
text = gutenberg.raw("austen-emma.txt")
words = re.findall(r"[a-z']+", text.lower())[:1000]
print("Corpus loaded!")
print("Total words:", len(words))
unigram = Counter(words)
bigram = Counter(zip(words, words[1:]))

trigram = Counter(zip(words, words[1:], words[2:]))
print("\nUNIGRAM - Top 5")
for x in unigram.most_common(5):
    print(x)
print("\nBIGRAM - Top 5")
for x in bigram.most_common(5):
    print(x)
print("\nTRIGRAM - Top 5")
for x in trigram.most_common(5):
    print(x)
print("\nProgram finished!")