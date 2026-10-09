
p_a = (3/4) * (2/3) * (2/3) * 1
p_b = (3/4) * (2/3) * (1/3) * 1 * 1

print("Sentence A probability:", round(p_a, 3))
print("Sentence B probability:", round(p_b, 3))

pp = p_a ** (-1/4)
print("Perplexity of A:", round(pp, 2))

