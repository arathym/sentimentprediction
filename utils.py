import re, nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

stemmer = PorterStemmer()


def get_filtered_text(text):
    return ' '.join(remove_stop_words(tokenize(text)))


def tokenize(text):
    # remove non letters
    text = re.sub("[^a-zA-Z]", " ", text.lower())
    # tokenize
    tokens = nltk.word_tokenize(text)
    # stem
    stems = stem_tokens(tokens)
    return stems


def stem_tokens(tokens):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed


def remove_stop_words(word_list):
    filtered_words = [word for word in word_list if word not in stopwords.words('english')]
    return filtered_words
