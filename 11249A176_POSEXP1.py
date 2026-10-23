# Program 1: Word Classes and Basic PoS Tagging using NLTK
import nltk
from nltk import word_tokenize, pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
sentence = input("Enter a sentence: ")
# Step 1: Tokenization
tokens = word_tokenize(sentence)
print("\nTokens:", tokens)
# Step 2: PoS Tagging
tagged = pos_tag(tokens)
print("\nWord\t\tPoS Tag")
print("-" * 30)
for word, tag in tagged:
 print(f"{word}\t\t{tag}")