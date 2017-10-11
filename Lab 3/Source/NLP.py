# -*- coding: utf-8 -*-
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
import nltk


# Function that tokenizes the input text
def tokenization(text):
    tokens = word_tokenize(text)
    print ('Tokenize')
    print (tokens, '\n')
    return tokens


# Function that removes stop words using English language
def stopWordsdeletion(tokens):
    stopWords = stopwords.words('english')
    filteredWords = [word for word in tokens if word not in stopWords]
    wordsWithoutStops = [word for word in filteredWords if len(word) > 2]
    print ('Filtered Words')
    print (wordsWithoutStops, '\n')
    return wordsWithoutStops


# Function that Lemmatizes the input paragraph
def lemmatization(nonstop):
    resultList = list()
    for j in nonstop:
        resultList.append(WordNetLemmatizer().lemmatize(j))
    print ('Lemmatized Words')
    print (resultList, '\n')
    return resultList


# Function to remove verbs from the paragraph
def verbsRemoval(lemwords):
    resultList = list()
    for j in pos_tag(lemwords):
        if j[1][:2] == 'VB':
            continue
        else:
            resultList.append(j[0])
    print ('Verb Removal')
    print (resultList, '\n')
    return resultList


# Function to calculate word frequency
def wordsFrequency(verbless):
    wordsFreq = nltk.FreqDist(verbless)
    topFive = dict()
    for w, f in wordsFreq.most_common(5):
        topFive[w] = f
    print ('Top Five Keys and Values')
    print (topFive, '\n')
    return topFive


# Function to get just top five words
def mostRepeatingwords(topfive):
    topFiveWords = topfive.keys()
    print ('Top Five Words')
    print (topFiveWords, '\n')
    return topFiveWords


# Function to find sentences with top five words
def sentenceFinder(text, topfive):
    result = list()
    for l in text.split('\n'):
        for w in topfive:
            if w in l.lower():
                result.append(l)
                break
    return result


# Function to summarize the sentence
def Summarizer(sentences):
    print ('Summarizing')
    print ('\n'.join(sentences))


def main():
    fileName = 'input.txt'
    text = open(fileName, "r").read()
    tokens = tokenization(text)
    nonstop = stopWordsdeletion(tokens)
    lemwords = lemmatization(nonstop)
    verbless = verbsRemoval(lemwords)
    topfive = wordsFrequency(verbless)
    topfivewords = mostRepeatingwords(topfive)
    sentences = sentenceFinder(text, topfivewords)
    Summarizer(sentences)

#Execution starts here

if __name__=="__main__":
    main()