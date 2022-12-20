import numpy as np
import math

def cal_ranking(dict_doc_words, dict_vocabulary_index, query_weight, dict_index_tfidf, proc_query):
    result = []
    weight_q = query_weight
    for doc in dict_doc_words.keys():
        doc_x_q = 0
        doc_norm = 0
        query_norm = math.sqrt(sum(i**2 for i in weight_q.values()))
        for word in set(proc_query):
            try:
                doc_x_q += dict_index_tfidf[(doc,
                                             dict_vocabulary_index[word])] * weight_q[word]
                doc_norm += (dict_index_tfidf[(doc,
                             dict_vocabulary_index[word])])**2
            except KeyError:
                pass

        a = (math.sqrt(doc_norm) * query_norm)
        if a == 0.0:
            sim = 0
        else:
            sim = doc_x_q / a
        result.append(sim)
    return result



def order_ranking(ranking,dic_doc_patch):
    merged_list = np.argsort(ranking)
    merged_list = np.flip(merged_list)
    path = []
    for i in merged_list:
        temp = (dic_doc_patch[i],ranking[i])
        path.append(temp)
    return path
















