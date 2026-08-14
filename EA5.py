import random

Customer = ["User"]
Action = ["browses products", "adds to cart", "places order", "makes payment"]

for i in range(5):
    print(random.choice(Customer), random.choice(Action))