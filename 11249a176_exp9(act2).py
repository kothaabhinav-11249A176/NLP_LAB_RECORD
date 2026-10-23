import nltk
sentence = "The teacher explains the lesson in the classroom."
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
words = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(words)
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    PP: {<IN><NP>}
"""
chunker = nltk.RegexpParser(grammar)
tree = chunker.parse(tagged_words)
print("Sentence:", sentence)
print("POS Tags:", tagged_words)
print("Chunk Tree:")
print(tree)
tree.draw()