# Program 2: Rule-Based PoS Tagging using Regular Expressions
import nltk
from nltk import word_tokenize
from nltk.tag import RegexpTagger
nltk.download('punkt')
# Hand-written rules (pattern, tag) applied in order
patterns = [
 (r'.*ing$', 'VBG'), # gerunds -> running
 (r'.*ed$', 'VBD'), # past tense -> jumped
 (r'.*es$', 'VBZ'), # 3rd person singular -> goes
 (r'.*ould$', 'MD'), # modals -> would, could
(r'.*\'s$', 'NN$'), # possessive nouns
 (r'.*s$', 'NNS'), # plural nouns
 (r'^-?[0-9]+(\.[0-9]+)?$', 'CD'), # cardinal numbers
 (r'(The|the|A|a|An|an)$', 'DT'), # determiners
 (r'(in|on|at|of|for|with)$', 'IN'),# prepositions
 (r'.*ly$', 'RB'), # adverbs
 (r'.*', 'NN'), # default: noun
]
rule_based_tagger = RegexpTagger(patterns)
sentence = input("Enter a sentence: ")
tokens = word_tokenize(sentence)
tagged_output = rule_based_tagger.tag(tokens)
print("\nWord\t\tPoS Tag (Rule-Based)")
print("-" * 35)
for word, tag in tagged_output:
 print(f"{word}\t\t{tag}")