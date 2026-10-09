
v = 20000
tokens = 10000000

bigrams = v ** 2
trigrams = v ** 3
fraction = tokens / trigrams

print("Possible bigrams:", bigrams)
print("Possible trigrams:", trigrams)
print("Maximum fraction:", fraction)

