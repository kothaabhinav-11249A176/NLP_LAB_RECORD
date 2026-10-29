from nltk.tag import RegexpTagger

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*', 'NN'),
    (r'.*ly$', 'RB')
]

tagger = RegexpTagger(patterns)
        
words = ["working", "quickly", "girl"]
print(tagger.tag(words))
