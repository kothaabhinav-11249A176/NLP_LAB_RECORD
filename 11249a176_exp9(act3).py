import nltk
sentence = "The young researcher develops an AI model."
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
words = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(words)
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""
chunker = nltk.RegexpParser(grammar)
tree = chunker.parse(tagged_words)
print("Sentence:", sentence)
print("POS Tagged Sequence:")
print(tagged_words)
print("\nChunked Sentence:")
print(tree)
tree.draw()