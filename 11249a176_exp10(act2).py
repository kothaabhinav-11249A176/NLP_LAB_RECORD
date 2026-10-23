import nltk
nltk.download('averaged_perceptron_tagger_eng')
sentence = "The students read their textbooks."
words = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(words)
grammar = r"""
NP: {<DT|PRP\$>?<JJ.*>*<NN.*>+}
"""
chunker = nltk.RegexpParser(grammar)
tree = chunker.parse(tags)
print("POS Tags:", tags)
print("Chunk Tree:")
print(tree)