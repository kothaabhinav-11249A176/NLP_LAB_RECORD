import nltk
from nltk import word_tokenize, pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentences = [
    "I like to run.",
    "I go for a run."
]

for sentence in sentences:
    print("\nSentence:", sentence)
    tokens = word_tokenize(sentence)
    tagged = pos_tag(tokens)

    for word, tag in tagged:
        if word.lower() == "run":
            print(word, "->", tag)

