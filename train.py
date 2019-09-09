import nltk
import sys
import subprocess
from subprocess import STDOUT
from glove import Glove
from glove import Corpus

def sentences():
    with open('../data/clean_wiki.txt', 'rt') as f:
        for i, sentence in enumerate(f.readlines()):
            sys.stdout.write('\rLoaded sentence #{}'.format(i))
            sys.stdout.flush()
            yield sentence.split()
        print('\n')

corpus = Corpus()
corpus.fit(sentences(), window=10)

glove = Glove(
            no_components=300,
            learning_rate=0.05
        )

glove.fit(corpus.matrix, epochs=25, no_threads=16, verbose=True)
glove.add_dictionary(corpus.dictionary)
print('added to dictionary')
glove.save('/home/x/xi/xinyuezhang/GloVe/model_2010wiki.glove')
print('model saved')
