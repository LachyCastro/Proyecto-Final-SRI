import numpy as np
def cal_ranking(dict_doc,dict_vocabulary_index,query,dict_index_tfidf, dict_word_idf):
    ranking = []

    for doc in dict_doc.keys():
        temp = 0
        for term in query:
            if term in dict_doc[doc]:# el termino de la query esta en el documneto
                index = dict_vocabulary_index[term]
                temp += dict_index_tfidf[index]*dict_word_idf[term]
        ranking.append(temp)
    return ranking

def order_ranking(ranking,dic_doc_patch):
    merged_list = np.argsort(ranking)
    merged_list = np.flip(merged_list)
    path = []
    for i in merged_list:
        path.append(dic_doc_patch[i])
    return path
















