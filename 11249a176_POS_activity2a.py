import nltk
from nltk import word_tokenize
from nltk.tag import RegexpTagger

nltk.download('punkt')

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*ly$', 'RB'),
    (r'.*ous$', 'JJ'),
    (r'.*ful$', 'JJ'),
    (r'.*ness$', 'NN'),
    (r'.*ment$', 'NN'),
    (r'.*', 'NN')
]

tagger = RegexpTagger(patterns)

paragraph = "The beautiful girl quickly finished her assignment. She was working carefully and happily."

tokens = word_tokenize(paragraph)

print(tagger.tag(tokens))