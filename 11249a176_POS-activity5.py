start_p = {'DT': 0.6, 'NN': 0.3, 'VB': 0.1}

trans_p = {
    'DT': {'DT': 0.05, 'NN': 0.85, 'VB': 0.10},
    'NN': {'DT': 0.10, 'NN': 0.30, 'VB': 0.60},
    'VB': {'DT': 0.40, 'NN': 0.50, 'VB': 0.10}
}

emit_p = {
    'DT': {'a': 0.5, 'the': 0.5},
    'NN': {'cat': 0.4, 'dog': 0.4, 'runs': 0.2},
    'VB': {'runs': 0.7, 'plays': 0.3}
}

words = ['a', 'cat', 'runs']
states = ['DT', 'NN', 'VB']

V = [{}]
path = {}

for s in states:
    V[0][s] = start_p[s] * emit_p[s].get(words[0], 0)
    path[s] = [s]

for t in range(1, len(words)):
    V.append({})
    new_path = {}

    for s in states:
        prob, prev = max(
            (V[t-1][p] * trans_p[p][s] *
             emit_p[s].get(words[t], 0), p)
            for p in states
        )
        V[t][s] = prob
        new_path[s] = path[prev] + [s]

    path = new_path

best = max(states, key=lambda s: V[-1][s])

print("Best tag sequence:", path[best])
print("Final probability:", V[-1][best])
