from .proc_query import *
from .proc_text import filter_words
from .load_files import load_corpus
from sklearn.feature_extraction.text import TfidfVectorizer
from .ranking import cal_ranking, order_ranking
import pickle
from .boolean import *
from .extended_boolean import *
from .utils import terms_query
from collections import Counter

# from proc_query import get_query_input_v
# from proc_text import filter_words
# from load_files import load_corpus
# from sklearn.feature_extraction.text import TfidfVectorizer
# from ranking import cal_ranking
# from ranking import order_ranking
# import pickle
# from boolean import *
# from extended_boolean import *
# from cran_parser import *
# from utils import terms_query
# from collections import Counter

load_c = True


def vectorial_model(query):
    if not load_c:
        load_corpus()
    splited_query = query.split()
    procesed_query = get_query_input_v(splited_query)

    pickle_1 = open('dic_vocabulary.txt', 'rb')
    vocabu = pickle.load(pickle_1)  # !dict{'word':index}
    pickle_2 = open('dic_word_idf.txt', 'rb')
    dic_word_idf = pickle.load(pickle_2)  # !dict{'word':idf}
    pickle_3 = open('dic_indx_tfidf.txt', 'rb')
    dic_indx_tfidf = pickle.load(pickle_3)  # !dict{index:tfidf}
    pickle_4 = open('dic_doc_words.txt', 'rb')
    dic_doc_words = pickle.load(pickle_4)  # !dict{doc:'words'}
    pickle_5 = open('dic_doc_path.txt', 'rb')
    dic_doc_patch = pickle.load(pickle_5)  # !dict{doc:'patch'}

    counter_dict = Counter(procesed_query)
    tf_query = calc_tf_query(counter_dict, procesed_query)
    query_weight = calc_weight_query(
        procesed_query, tf_query, dic_word_idf)
    rank = cal_ranking(dic_doc_words, vocabu, query_weight,
                       dic_indx_tfidf, procesed_query)
    orded_rank = order_ranking(rank, dic_doc_patch)
    return orded_rank


def boolean_model(query):
    if not load_c:
        charge_corpus()
    pickle_1 = open('dic_vocabulary.txt', 'rb')
    pickle_4 = open('dic_doc_words.txt', 'rb')
    dic_doc_words = pickle.load(pickle_4)  # !dict{doc:'words'}
    pickle_5 = open('dic_doc_path.txt', 'rb')
    dic_doc_patch = pickle.load(pickle_5)  # !dict{doc:'patch'}
    documents = valid_documents(dic_doc_words, dic_doc_patch, query)
    return documents


def extended_boolean_model(query, is_eval):
    if not load_c:
        charge_corpus()
    pickle_1 = open('dic_vocabulary.txt', 'rb')
    vocabu = pickle.load(pickle_1)  # !dict{'word':index}
    pickle_3 = open('dic_indx_tfidf.txt', 'rb')
    dic_indx_tfidf = pickle.load(pickle_3)  # !dict{index:tfidf}
    pickle_4 = open('dic_doc_words.txt', 'rb')
    dic_doc_words = pickle.load(pickle_4)  # !dict{doc:'words'}
    pickle_5 = open('dic_doc_path.txt', 'rb')
    dic_doc_patch = pickle.load(pickle_5)  # !dict{doc:'patch'}
    pickle_6 = open('dic_doc_ind_tfidf.txt', 'rb')
    if not is_eval:

        query = evaluate_query(to_dnf(query).__str__())
    document_rank = extended_ranking(
        dic_doc_words, vocabu, query, dic_indx_tfidf)
    order_rank = order_ranking(document_rank, dic_doc_patch)
    return order_rank


def charge_corpus():
    text, dic_doc_path = load_corpus(
        'C:/Users/acer/Downloads/Telegram Desktop/vaswani/vaswani')
    tfidf = TfidfVectorizer()
    filter_text = []
    count = 0
    for t in text:
        filter_text.append(filter_words(t, False))
        print(count)
        count += 1

    # aqui se guardaa para cada dcoumento la lista de terminos d ese documento #! dicc2
    dict_doc_words = {}
    for i in range(len(filter_text)):
        dict_doc_words[i] = [word for word in filter_text[i].split()]
    result_ = tfidf.fit_transform(filter_text)
    # aqui se guarda indeice vs tfidf #! dicc3
    # dic_indx_tfidf = {i: d for i, d in zip(indx, data)}
    dic_indx_tfidf = result_
    vocabu = tfidf.vocabulary_  # aqui se guarda nombre vs indice #! dicc4
    dic_word_idf = {}  # aqui se guarda para cada palabra su idf asociado #! dicc1
    for ele1, ele2 in zip(tfidf.get_feature_names_out(), tfidf.idf_):
        dic_word_idf[ele1] = ele2
    print("--------------------------------------------------------------aqui")
    with open('dic_indx_tfidf.txt', 'wb') as fh:
        pickle.dump(dic_indx_tfidf, fh)
        fh.close()
    with open('dic_doc_words.txt', 'wb') as fh:
        pickle.dump(dict_doc_words, fh)
        fh.close()
    with open('dic_vocabulary.txt', 'wb') as fh:
        pickle.dump(vocabu, fh)
        fh.close()
    with open('dic_word_idf.txt', 'wb') as fh:
        pickle.dump(dic_word_idf, fh)
        fh.close()
    with open('dic_doc_path.txt', 'wb') as fh:
        pickle.dump(dic_doc_path, fh)
        fh.close()
    load_c = True


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
