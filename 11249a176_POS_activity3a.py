import nltk
from nltk.corpus import brown
from nltk import UnigramTagger, BigramTagger

nltk.download('brown')

tagged_sentences = brown.tagged_sents(categories='news')

size = int(len(tagged_sentences) * 0.9)  # Try 0.9, then 0.5

train_data = tagged_sentences[:size]
test_data = tagged_sentences[size:]

unigram_tagger = UnigramTagger(train_data)
bigram_tagger = BigramTagger(train_data, backoff=unigram_tagger)

print('Unigram accuracy:', unigram_tagger.accuracy(test_data))
print('Bigram accuracy :', bigram_tagger.accuracy(test_data))

