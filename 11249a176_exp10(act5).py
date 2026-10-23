import nltk
nltk.download('averaged_perceptron_tagger_eng')
sentence = "The young scientist is developing a new application."
words = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(words)
grammar = r"""
NP: {<DT>?<JJ.*>*<NN.*>+}
VP: {<VB.*><VB.*>*}
"""
chunker = nltk.RegexpParser(grammar)
tree = chunker.parse(tags)
print("POS Tags:", tags)
print("Improved Chunk Tree:")
print(tree)