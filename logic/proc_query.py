# from proc_text import filter_words
from .proc_text import filter_words
import pickle


def get_query_input(str_q):
    #     # final_query = []
    query = filter_words(str_q, True).split()
#     # pickle_1 = open('dic_vocabulary.txt', 'rb')
#     # vocabu: dict = pickle.load(pickle_1)
#     # no se deberia quitar las palabras q no estan en los dic, luego en el calculo del peso su idf sera 0 y listo
#     # for word in query:#!aqui deberiamos comprobar q la palabras q no sten en los terminos desecharlas !!!!!!!!!!!!!!!!!!!duda aki!!!!!!!!!!!!!!!!!!!!!!!
#     #     if word in vocabu.keys():
#     #         final_query.append(word)
    return query


def get_query_input_v(splited_query):
    for i, word in enumerate(splited_query):
        l_word = filter_words(word, True)
        if len(l_word) > 0:
            p_word = l_word[:len(l_word) - 1]
            splited_query[i] = p_word
    return splited_query
