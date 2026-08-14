import re
from nltk import FreqDist
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
words = re.findall(r"[a-z']+", corpus.lower())
freq = FreqDist(words)
N = len(words)
print("Word\tCount\tProbability")
for word, count in freq.most_common():
    probability = count / N
    print(word, "\t", count, "\t", round(probability, 4))
word = "fox"
print("\nP('fox') =", round(freq[word] / N, 4))