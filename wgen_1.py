words = {
    "box": "boxes",
    "city": "cities",
    "child": "children",
    "boy": "boys",
    "bus": "buses",
    "knife": "knives"
}
# (a) Generate plural forms
for word, plural in words.items():
    print(word, "->", plural)
# (b) Rules and exceptions
print("General rule: Add s or es, change y to ies")
print("Exception: child -> children")