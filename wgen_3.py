
# (a) Intermediate forms
print("cat+N+PL -> cat^s#")
print("fox+N+PL -> fox^s#")

# (b) and (c) Apply plural rule
words = ["fox", "cat", "church", "wish", "boy"]

for word in words:
    if word.endswith(("x", "ch", "sh", "s", "z")):
        plural = word + "es"
    else:
        plural = word + "s"
    print(word, "->", plural)

# (d) Reverse transducer
print("Reverse mapping converts surface forms to lexical forms.")