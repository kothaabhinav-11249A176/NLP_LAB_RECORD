import re
text = "The cat sat on the mat. The dog sat on the log."
tokens = re.findall(r"\b\w+\b", text)
# (a) Count word tokens
print("(a) Word Tokens:", len(tokens))
# (b) Count word types
lower_types = set(word.lower() for word in tokens)
case_types = set(tokens)
print("(b) Lowercase Word Types:", len(lower_types))
print("    Case-preserved Word Types:", len(case_types))
# (c) Calculate TTR
ttr = len(lower_types) / len(tokens)
print("(c) Type-Token Ratio:", round(ttr, 4))
# (d) Explain why TTR is a poor comparison measure
print("(d) TTR decreases as text length increases,")
print("    so it cannot fairly compare texts of different lengths.")