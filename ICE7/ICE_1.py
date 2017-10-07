from nltk import pos_tag, ne_chunk
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer


def FindMeanings(sentence):
    from nltk.corpus import wordnet as wn
    tokens = sentence.split()
    synsets = wn.synsets(tokens[2])
    print 'WordNet'
    print[str(syns.definition) for syns in synsets], '\n'


def Tokenize(sentence):
    print 'Tokenize'
    print sent_tokenize(sentence), '\n'


def Stem(sentence):
    stems = PorterStemmer()
    word = sentence.split()
    print 'Stemming'
    print stems.stem(word[12]), '\n'


def FindPOS(sentence):
    from nltk.tag import pos_tag
    words = word_tokenize(sentence)
    print 'POS'
    print pos_tag(words), '\n'


def Lemmatize(sentence):
    lemmatizer = WordNetLemmatizer()
    splitwords = sentence.split()
    print 'Lemmatize'
    print lemmatizer.lemmatize(splitwords[12], pos='v'), '\n'


def Trigram(sentence):
    from  nltk.util import ngrams
    token = word_tokenize(sentence.lower())
    print 'Trigram'
    for i in ngrams(token, 3):
        print i
    print '\n'


def EntityRecognizer(sentence):
    print 'EntityRecognizer'
    print ne_chunk(pos_tag(wordpunct_tokenize(sentence)))


print 'NLP'
text = open("input.txt", "r").read()

FindMeanings(text)
Tokenize(text)
Stem(text)
FindPOS(text)
Lemmatize(text)
Trigram(text)
EntityRecognizer(text)