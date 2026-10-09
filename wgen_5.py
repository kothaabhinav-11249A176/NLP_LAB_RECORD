# (a) Valid derived words
words = {
    "un + lock + able": "unlockable",
    "happy + ness": "happiness",
    "employ + ment": "employment",
    "modern + ize": "modernize",
    "re + write + ing": "rewriting"
}
for word, result in words.items():
    print(word, "->", result)
# (b) Invalid words
print("employness -> Rejected")
print("unhappyable -> Rejected")
# (c) Ambiguous word
print("unlockable: not lockable OR able to be unlocked")
# (d) Simple filter
print("Use dictionary and word-category rules.")