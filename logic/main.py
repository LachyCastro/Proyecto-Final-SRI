import pathlib
from time import time
from numpy import char
from .proc_text import filter_words
from .load_files import load_corpus
from sklearn.feature_extraction.text import TfidfVectorizer
from .ranking import cal_ranking
from .ranking import order_ranking
import pickle

#tODO testing load files
load_c = True

def vectorial_model(query):
    if not load_c:
        charge_corpus()
    q = query
    
    print("--------------------------------------------------------------aqui1")
    pickle_1 = open('dic_vocabulary.txt','rb')
    vocabu = pickle.load(pickle_1)					#!dict{'word':index}
    pickle_2 = open('dic_word_idf.txt','rb')
    dic_word_idf = pickle.load(pickle_2)			#!dict{'word':idf}
    pickle_3 = open('dic_indx_tfidf.txt','rb')
    dic_indx_tfidf = pickle.load(pickle_3)			#!dict{index:tfidf}
    pickle_4 = open('dic_doc_words.txt','rb')
    dic_doc_words = pickle.load(pickle_4)           #!dict{doc:'words'}
    pickle_5 = open('dic_doc_path.txt','rb')       
    dic_doc_patch = pickle.load(pickle_5)			#!dict{doc:'patch'}
    print("--------------------------------------------------------------aqui2")

    vect_query = {}
    for term in q:
        vect_query[vocabu[term]] = dic_word_idf[term]
    rank = cal_ranking(dic_doc_words,vocabu,q,dic_indx_tfidf,dic_word_idf)
    orded_rank = order_ranking(rank, dic_doc_patch)#Ordena los path del ranking
    print(orded_rank)
   
    #se queda con la cantidad que se decidan mostrar y los retorna
    documents =[]    
    count = 0
    for path in orded_rank:
        if count == 10:
            break
       
        documents.append(path)
        count += 1

    print(documents.__len__(), 'documentosssssssssssssssssssssssssssssssssssss')
    return documents
    



def charge_corpus():
    text, dic_doc_path = load_corpus('C:/Users/lachy/Videos/LACHY/Proyecto Final SRI/corpus')
    #text = load_corpus('C:/Users/acer/Downloads/Telegram Desktop/SRI/corpus') #PC rainel
    tfidf = TfidfVectorizer()
    filter_text = []
    count = 0
    for t in text:
        filter_text.append(filter_words(t))
        print(count)
        count+=1
        if count == 10:
            break
    
    dict_doc_words = {} #aqui se guardaa para cada dcoumento la lista de terminos d ese documento #! dicc2
    for i in range(len(filter_text)):
        dict_doc_words[i] = [word for word in filter_text[i].split()]
    result_ = tfidf.fit_transform(filter_text)
    data = result_.data
    indx = result_.indices
    dic_indx_tfidf = {i:d for i,d in zip(indx,data)} #aqui se guarda indeice vs tfidf #! dicc3
    vocabu = tfidf.vocabulary_# aqui se guarda nombre vs indice #! dicc4
    dic_word_idf = {} #aqui se guarda para cada palabra su idf asociado #! dicc1
    for ele1, ele2 in zip(tfidf.get_feature_names_out(), tfidf.idf_):
        dic_word_idf[ele1] = ele2
    print("--------------------------------------------------------------aqui")
    with open('dic_indx_tfidf.txt','wb') as fh:
        pickle.dump(dic_indx_tfidf,fh)
        fh.close()
    with open('dic_doc_words.txt','wb') as fh:
        pickle.dump(dict_doc_words,fh)
        fh.close()
    with open('dic_vocabulary.txt','wb') as fh:
        pickle.dump(vocabu,fh)
        fh.close()
    with open('dic_word_idf.txt','wb') as fh:
        pickle.dump(dic_word_idf,fh)
        fh.close()
    with open('dic_doc_path.txt','wb') as fh:
        pickle.dump(dic_doc_path,fh)
        fh.close()
    load_c = True