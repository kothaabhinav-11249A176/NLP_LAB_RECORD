import re
text = "Kal ka meeting cancel ho gaya, please reschedule it by Friday."
hindi_words = {"kal", "ka", "ho", "gaya"}
# (a) Tokenize and label language
tokens = re.findall(r"\b\w+\b", text)
print("(a) Token Language Labels:")
for token in tokens:
    language = "HI" if token.lower() in hindi_words else "EN"
    print(token, "->", language)
# (b) Why English analysis fails
print("\n(b) Reasons:")
print("1. Hindi words have different grammar and meanings.")
print("2. Romanised Hindi and English are mixed together.")
# (c) Preprocessing pipeline
print("\n(c) Preprocessing Pipeline:")
print("1. Tokenization")
print("2. Language identification")
print("3. Spelling normalisation")
print("4. Hindi and English lemmatization")
print("5. POS tagging and text analysis")
# (d) Benefit
print("\n(d) Language-aware processing improves")
print("    analysis of code-mixed text.")
