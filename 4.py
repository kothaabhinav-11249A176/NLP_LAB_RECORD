s = "cat"
state = 0
for c in s:
    if state == 0 and c == "c":
        state = 1
    elif state == 1 and c == "a":
        state = 2
    elif state == 2 and c == "t":
        state = 3
    else:
        state = 0
print("Accepted" if state == 3 else "Rejected")