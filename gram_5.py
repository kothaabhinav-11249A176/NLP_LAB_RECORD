
import math

p = 1
for i in range(100):
    p *= 10 ** -4

print("Probability:", p)
print("Log probability:", round(100 * math.log(10 ** -4), 2))
print("Suitable n-gram: Character n-gram")
