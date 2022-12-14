import nltk
from nltk.tokenize import word_tokenize
from nltk import ne_chunk, pos_tag
from nltk.corpus import stopwords
import string
import re
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")


def __replace(text):
    s = text
    for (pattern, repl) in __replacement_patterns:
        s = re.sub(pattern, repl, s)
    return s


def entities(text):
    return ne_chunk(
        pos_tag(
            word_tokenize(text)))


def __tokenize_and_stem(text):
    tokens = [word for word in nltk.word_tokenize(text)]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems


__replacement_patterns = [(r'[wW]on\'t', 'will not'),
                          (r'[cC]an\'t', 'can not'),
                          (r'[iI]\'m', 'i am'),
                          (r'[aA]in\'t', 'is not'),
                          (r'[iI]t\'s', 'it is'),
                          (r'(\w+)\'ll', '\g<1> will'),
                          (r'(\w+)n\'t', '\g<1> not'),
                          (r'(\w+)\'ve', '\g<1> have'),
                          (r'(\w+)\'s', '\g<1>'),
                          (r'(\w+)\'re', '\g<1> are'),
                          (r'(\w+)\'em', '\g<1> them'),
                          (r'[nN]\'t', 'not'),
                          (r'\'m', 'am'),
                          (r'\'s', 'is'),
                          (r'\'ll', 'will'),
                          (r'\'ve', 'have'),
                          (r'\'re', 'are'),
                          (r'&', 'and'),
                          (r'%', 'percent')]


stop_words = set(stopwords.words('english'))


def repleace_contractions(lines):
    f1_words = __replace(lines)
    return f1_words


def stem_tokens(f1_words):
    # este metodo lleva las palabrasa su raiz
    words_tokens = __tokenize_and_stem(f1_words)
    return words_tokens


def repleace_punctuation_marks(words_tokens):
    f2_words = list(
        filter(lambda token: token not in string.punctuation, words_tokens))
    return f2_words


def eliminate_stop_words(f2_words):
    f3_words = list(filter(lambda token: token not in stop_words, f2_words))
    return f3_words


def classify_words(f3_words):
    f4_words = nltk.pos_tag(f3_words)
    return f4_words


important_words = ['FW', 'JJ', 'JJR', 'JJS', 'MD', 'NN', 'NNS',
                   'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


def filter_important_words(f4_words, is_query) -> str:
    """_summary_

    Args:
        f4_words (_type_): _description_

    Returns:
        str: Devuelve un string con cada palabra separada por espacio
    """
    if is_query:
        f5_words = list(
            filter(lambda token: token[1] in important_words, f4_words))
    else:
        f5_words = set(
            filter(lambda token: token[1] in important_words, f4_words))
    result = ''
    for tup in f5_words:
        result += tup[0] + ' '
    return result


def filter_words(lines, is_query):
    f1 = repleace_contractions(lines)
    f2 = stem_tokens(f1)
    f3 = repleace_punctuation_marks(f2)
    f4 = eliminate_stop_words(f3)
    f5 = classify_words(f4)
    f6 = filter_important_words(f5, is_query)
    return f6
