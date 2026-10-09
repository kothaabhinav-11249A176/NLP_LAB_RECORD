import re
text = "OMG!! Can't wait for #NLP2026 @IITM :) Tickets cost $4.5k, e-mail me at ravi@example.com"
# (a) Whitespace tokenization
print("(a) Whitespace Tokens:")
print(text.split())
# (b) Better tokenization
pattern = r"""[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}|:\)|:-\)|:\(|:-\(|[$]\d+(?:\.\d+)?[kKmM]?|#[A-Za-z0-9_]+|@[A-Za-z0-9_]+|n't|'re|'ve|'ll|'d|'m|'s|[A-Za-z]+(?:-[A-Za-z]+)*|\d+(?:\.\d+)?|[^\w\s]"""
tokens = re.findall(pattern, text)
print("\n(b) Better Tokens:")
print(tokens)
# (c) Penn Treebank convention
print("\n(c) Can't is split into 'Ca' and \"n't\".")
print("    Penn Treebank separates many contractions.")
# (d) Importance of good tokenization
print("\n(d) Good tokenization preserves hashtags, mentions,")
print("    emoticons, email addresses, and currency amounts.")