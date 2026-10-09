forms = {
    "PL": "மரங்கள்",
    "ACC": "மரத்தை",
    "PL+ACC": "மரங்களை"
}
# (a), (b) Generate Tamil noun forms
for tag, word in forms.items():
    print("மரம் +", tag, "->", word)
# (c) Paradigm classes and sandhi rules
print("Paradigm classes handle noun patterns.")
print("Sandhi rules handle sound changes.")