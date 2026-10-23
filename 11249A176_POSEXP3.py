# Program 3: Stochastic PoS Tagging using Unigram + Bigram (Statistical) Tagger
import nltk
from nltk.corpus import brown
from nltk import UnigramTagger, BigramTagger, word_tokenize
nltk.download('brown')
nltk.download('punkt')
# Step 1: Load tagged sentences from the Brown corpus
tagged_sentences = brown.tagged_sents(categories='news')
# Step 2: Split into training and testing data (90% / 10%)
size = int(len(tagged_sentences) * 0.9)
train_data = tagged_sentences[:size]
test_data = tagged_sentences[size:]
# Step 3: Train Unigram tagger, then Bigram tagger backed off to Unigram
unigram_tagger = UnigramTagger(train_data)
bigram_tagger = BigramTagger(train_data, backoff=unigram_tagger)
# Step 4: Evaluate accuracy on test data
accuracy = bigram_tagger.accuracy(test_data)
print(f"Tagger Accuracy on Test Data: {accuracy * 100:.2f}%")
# Step 5: Tag a new sentence
sentence = input("\nEnter a sentence: ")
tokens = word_tokenize(sentence)
result = bigram_tagger.tag(tokens)
print("\nWord\t\tPoS Tag (Stochastic)")
print("-" * 35)
for word, tag in result:
 print(f"{word}\t\t{tag}")
