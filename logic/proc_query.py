# from proc_text import filter_words
from .proc_text import filter_words
import pickle


def get_query_input(str_q):
    query = filter_words(str_q, True).split()
    return query


def get_query_input_v(splited_query):
    for i, word in enumerate(splited_query):
        l_word = filter_words(word, True)
        if len(l_word) > 0:
            p_word = l_word[:len(l_word) - 1]
            splited_query[i] = p_word
    return splited_query


def calc_weight_query(procesed_query, tf_query, dic_word_idf):
    result = {}
    for word in procesed_query:
        try:
            result[word] = (0.4 + (1 - 0.4) * tf_query[word]) * \
                dic_word_idf[word]
        except:
            result[word] = 0
    return result


def calc_tf_query(counter_dict, procesed_query):
    tf_query = {}
    qq = counter_dict.most_common(1)[0][1]
    for word in procesed_query:
        tf_query[word] = counter_dict[word] / counter_dict.most_common(1)[0][1]
    return tf_query
