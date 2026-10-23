# Program 5(b): PoS Tagging using HMM with a hand-coded Viterbi Algorithm
# States
states = ['DT', 'NN', 'VB']
# Initial probabilities
start_p = {'DT': 0.6, 'NN': 0.3, 'VB': 0.1}
# Transition probabilities
trans_p = {
    'DT': {'DT': 0.05, 'NN': 0.85, 'VB': 0.10},
    'NN': {'DT': 0.10, 'NN': 0.30, 'VB': 0.60},
    'VB': {'DT': 0.40, 'NN': 0.50, 'VB': 0.10}
}
# Emission probabilities
emit_p = {
    'DT': {'the': 0.7, 'a': 0.3},
    'NN': {'dog': 0.4, 'cat': 0.4, 'bites': 0.05, 'runs': 0.15},
    'VB': {'bites': 0.6, 'runs': 0.4}
}
def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
    # Initialization
    for st in states:
        V[0][st] = start_p[st] * emit_p[st].get(obs[0], 1e-6)
        path[st] = [st]
    # Recursion
    for t in range(1, len(obs)):
        V.append({})
        new_path = {}
        for cur in states:
            best_prob, best_prev = max(
                (
                    V[t - 1][prev]
                    * trans_p[prev][cur]
                    * emit_p[cur].get(obs[t], 1e-6),
                    prev
                )
                for prev in states
            )
            V[t][cur] = best_prob
            new_path[cur] = path[best_prev] + [cur]
        path = new_path
    # Termination
    n = len(obs) - 1
    best_final_prob, best_final_st = max(
        (V[n][st], st) for st in states
    )
    return best_final_prob, path[best_final_st]
# Input sentence
sentence = ['the', 'dog', 'bites']
# Run Viterbi algorithm
prob, tag_sequence = viterbi(
    sentence, states, start_p, trans_p, emit_p
)
print("Sentence :", sentence)
print("Best Tag Sequence :", tag_sequence)
print(f"Probability : {prob:.6f}")