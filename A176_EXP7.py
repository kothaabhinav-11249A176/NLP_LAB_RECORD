import re
training = """the quick brown fox jumps over the lazy dog
the dog barks at the fox"""
vocabulary = set(re.findall(r"[a-z']+", training.lower()))
test = "the fox runs with a cat"
words = re.findall(r"[a-z']+", test.lower())
oov_words = [word for word in words if word not in vocabulary]
oov_rate = len(oov_words) / len(words) * 100
print("Test sentence:", test)
print("OOV words:", oov_words)
print("OOV count:", len(oov_words))
print("Total words:", len(words))
print("OOV Rate:", round(oov_rate, 2), "%")