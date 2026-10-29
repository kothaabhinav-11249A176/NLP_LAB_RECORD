from nltk import UnigramTagger, BigramTagger

nltk.download('brown')

train = brown.tagged_sents(categories='news')
news_test = train[int(len(train) * 0.9):]
train = train[:int(len(train) * 0.9)]

romance_test = brown.tagged_sents(categories='romance')

uni = UnigramTagger(train)
bi = BigramTagger(train, backoff=uni)

print("News accuracy:", bi.accuracy(news_test))
print("Romance accuracy:", bi.accuracy(romance_test))
