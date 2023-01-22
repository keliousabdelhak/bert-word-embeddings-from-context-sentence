

from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'

DESCRIPTION = 'Extract bert word embedding from sentence (based on the context)'
LONG_DESCRIPTION = 'A package that allows to build word embedding from context using bert, To extract BERT word embeddings from a sentence, you would first need to tokenize the sentence and then input the tokens into a pre-trained BERT model. The model will then generate a fixed-length vector representation for each token, known as the word embedding, based on the context of the sentence. These embeddings can then be used for various natural language processing tasks such as text classification and sentiment analysis.'

# Setting up
setup(
    name="word-embeddings-from-context",
    version=VERSION,
    author="Abdelhak KELIOUS",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['torch', 'pytorch-pretrained-bert'],
    keywords=['python', 'nlp', 'bert', 'text', 'transformers', 'embedding', 'word embedding', 'sentence embedding', 'context embedding', 'word embedding from context', 'sentence embedding from context', 'context embedding from context','similarity'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)