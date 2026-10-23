import nltk
sentences = [
    "a student",
    "the very intelligent student"
]
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
grammar = r"""
    NP: {<DT>?<RB.*>*<JJ.*>*<NN.*>+}
"""
chunker = nltk.RegexpParser(grammar)
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(words)
    tree = chunker.parse(tagged_words)
    print("\nSentence:", sentence)
    print("POS Tags:", tagged_words)
    print("Chunk Tree:")
    print(tree)