text = "Students learn Python programming"
w = text.split()
for i in range(len(w)-1):
    print((w[i], w[i+1]))