import nltk
from nltk import word_tokenize, pos_tag
from collections import Counter

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "The smart boy quickly reads interesting books and writes stories."

tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

counts = Counter()

for word, tag in tagged:
    if tag.startswith('NN'):
        counts['Noun'] += 1
    elif tag.startswith('VB'):
        counts['Verb'] += 1
    elif tag.startswith('JJ'):
        counts['Adjective'] += 1
    elif tag.startswith('RB'):
        counts['Adverb'] += 1

print("Category counts:")
for category, count in counts.items():
    print(category, ":", count)

print("Most frequent category:", counts.most_common(1)[0][0])