# Zipf's Law: f = k / r
k = 120000
# (a) Frequencies at ranks 2, 10 and 100
print("(a) Rank 2:", k / 2)
print("    Rank 10:", k / 10)
print("    Rank 100:", k / 100)
# (b) Frequency at rank 50000
print("\n(b) Rank 50000:", k / 50000)
# (c) Meaning of the long tail
print("\n(c) Many words occur rarely, making them")
print("    difficult for a model to learn reliably.")