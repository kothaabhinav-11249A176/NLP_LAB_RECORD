def perplexity(prob, n):
 return prob ** (-1 / n) if prob > 0 else float("inf")
test_sentence = "the fox runs away"
n = len(test_sentence.split())
uni_p = 0.0009
bi_p = 0.00021
tri_p = 0.00007
print("Unigram Perplexity:", round(perplexity(uni_p, n), 2))
print("Bigram Perplexity:", round(perplexity(bi_p, n), 2))
print("Trigram Perplexity:", round(perplexity(tri_p, n), 2))