import re
import matplotlib.pyplot as plt
from collections import Counter
text = """Natural language processing is a field of artificial intelligence.
It helps computers understand human language.
Language models are used in many applications."""
words = re.findall(r"[a-z']+", text.lower())
unigram = Counter(words)
top10 = unigram.most_common(10)
words = [x[0] for x in top10]
counts = [x[1] for x in top10]
plt.bar(words, counts)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top 10 Unigrams")
plt.xticks(rotation=45)
plt.show()
