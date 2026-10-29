from nltk import word_tokenize
from nltk.tag import RegexpTagger

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*ly$', 'RB'),
    (r'.*', 'NN')
]

tagger = RegexpTagger(patterns)

paragraph = "She was working carefully."
tokens = word_tokenize(paragraph)

print(tagger.tag(tokens))

