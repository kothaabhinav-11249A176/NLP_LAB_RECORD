from nltk.tag import brill, brill_trainer
from nltk import UnigramTagger

baseline_tagger = UnigramTagger(train_data)
templates = brill.brill24()

trainer = brill_trainer.BrillTaggerTrainer(
    baseline_tagger, templates, trace=0
)

brill_tagger = trainer.train(train_data, max_rules=10)

print('Baseline accuracy:', baseline_tagger.accuracy(test_data))
print('Brill accuracy   :', brill_tagger.accuracy(test_data))
