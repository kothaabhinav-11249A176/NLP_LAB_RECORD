# Program 4: Transformation-Based Tagging using Brill Tagger (NLTK)
import nltk
from nltk.corpus import brown
from nltk import UnigramTagger, word_tokenize
from nltk.tag.brill import Word, Pos
from nltk.tag import brill, brill_trainer
nltk.download('brown')
nltk.download('punkt')
tagged_sentences = brown.tagged_sents(categories='news')
size = int(len(tagged_sentences) * 0.9)
train_data = tagged_sentences[:size]
test_data = tagged_sentences[size:]
# Step 1: Initial baseline tagger
baseline_tagger = UnigramTagger(train_data)
print(f"Baseline (Unigram) Accuracy: {baseline_tagger.accuracy(test_data)*100:.2f}%")
# Step 2: Define transformation rule templates
templates = brill.brill24()
# Step 3: Train the Brill (transformation-based) tagger
trainer = brill_trainer.BrillTaggerTrainer(baseline_tagger, templates, trace=3)
brill_tagger = trainer.train(train_data, max_rules=20)
# Step 4: Evaluate the transformation-based tagger
print(f"\nBrill Tagger Accuracy: {brill_tagger.accuracy(test_data)*100:.2f}%")
# Step 5: Tag a new sentence
sentence = input("\nEnter a sentence: ")
tokens = word_tokenize(sentence)
print("\nTagged Output:", brill_tagger.tag(tokens))