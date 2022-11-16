from .proc_text import filter_words
import pickle

def get_query_input(str_q):
    final_query = []
    query = filter_words(str_q).split()
    pickle_1 = open('dic_vocabulary.txt','rb')
    vocabu : dict = pickle.load(pickle_1)
    for word in query:#aqui deberiamos comprobar q la palabras q no sten en los terminos desecharlas
        if word in vocabu.keys():
            final_query.append(word)

    return final_query




