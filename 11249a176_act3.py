import nltk
sentences = [
    "I read a book.",
    "Please book a ticket.",
    "Children play football.",
    "We watched a play."
]
for sentence in sentences:
    print("\nSentence:", sentence)
    tokens = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(tokens)
    print(tagged_words)