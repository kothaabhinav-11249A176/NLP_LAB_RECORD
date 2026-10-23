import nltk
nltk.download('averaged_perceptron_tagger_eng')
sentence = "The student reads a book in the library."
words = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(words)
grammar1 = r"""
NP: {<DT>?<JJ.*>*<NN.*>+}
"""
grammar2 = r"""
NP: {<DT>?<JJ.*>*<NN.*>+}
PP: {<IN><NP>}
VP: {<VB.*><NP>?}
"""
chunker1 = nltk.RegexpParser(grammar1)
chunker2 = nltk.RegexpParser(grammar2)
tree1 = chunker1.parse(tags)
tree2 = chunker2.parse(tags)
print("NP Only:")
print(tree1)
print("\nNP + VP + PP:")
print(tree2)