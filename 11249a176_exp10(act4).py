import nltk
nltk.download('averaged_perceptron_tagger_eng')
sentences = [
    "The student reads a book in the library.",
    "The professor teaches computer science in the classroom.",
    "The students play football on the ground.",
    "A researcher develops a model in the laboratory.",
    "The librarian keeps the books on the shelf."
]
grammar = r"""
NP: {<DT>?<JJ.*>*<NN.*>+}
PP: {<IN><NP>}
VP: {<VB.*><NP>?}
"""
chunker = nltk.RegexpParser(grammar)
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)
    tree = chunker.parse(tags)
    print("\nSentence:", sentence)
    print(tree)