from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk
nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
words = ["running", "ran", "runs", "runner", "runners"]
# (a) Lemma of each word
print("(a) Lemmas:")
for word in words:
    print(word, "->", lemmatizer.lemmatize(word, pos="v"))
# (b) Porter stemming
print("\n(b) Porter Stems:")
for word in words:
    print(word, "->", stemmer.stem(word))
# (c) Recall and precision
print("\n(c) Stemming often improves recall.")
print("    Lemmatization often improves precision.")
# (d) Extra input required
print("\n(d) A lemmatizer may require POS tags,")
print("    a dictionary, and morphological information.")