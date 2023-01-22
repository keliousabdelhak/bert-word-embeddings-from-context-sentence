

from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'

DESCRIPTION = 'Extract bert word embedding from sentence (based on the context)'
LONG_DESCRIPTION = 'A package that allows to build word embedding from context using bert, To extract BERT word embeddings from a sentence, you would first need to tokenize the sentence and then input the tokens into a pre-trained BERT model. The model will then generate a fixed-length vector representation for each token, known as the word embedding, based on the context of the sentence. These embeddings can then be used for various natural language processing tasks such as text classification and sentiment analysis.'

# Setting up
setup(
    name="word_embeddings_from_context",
    version=VERSION,
    author="Abdelhak KELIOUS",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
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