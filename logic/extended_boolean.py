from .proc_text import *
import math
from sympy.logic.boolalg import to_dnf
def extended_ranking(dic_doc_words,vocabu,query,dic_doc_ind_tfidf):
    terms = terms_query(query)
    ranking = []
    query = evaluate_query(to_dnf(query).__str__(), terms)
    # aqui va el if de si solo hay que hacer or 
    for doc in dic_doc_words.keys():
        operands_for_or = []
        for component in query:
            operands_for_and = []
            x = component.split()# hay q splitear para convertir en array pq si no toma letra por letra
            for term in x:
                if term in dic_doc_words[doc]:# el termino de la query esta en el documneto
                   index_term = vocabu[term]
                   operands_for_and.append(dic_doc_ind_tfidf[(doc,index_term)])
                else:
                    operands_for_and.append(0)
            if len(x) > 1 :
                operands_for_or.append(evaluate_and_operator(operands_for_and))
            else:
                operands_for_or.append(operands_for_and[0])
        ranking.append(evaluate_or_operator(operands_for_or))
    return ranking

def terms_query(query): #Pasar a utils q esta repetido para el booleano extendido, estos son los terminos por donde iterar
    terms = query.replace('(', '')
    terms = terms.replace(')', '')
    terms = terms.replace('and', '')
    terms = terms.replace('not', '')
    terms = terms.replace('or', '')
    f1 = repleace_contractions(terms)
    f2 = stem_tokens(f1)
    f3 = repleace_punctuation_marks(f2)
    f4 = eliminate_stop_words(f3)
    return f4

def evaluate_and_operator(operands):
    return 1.0 - math.sqrt(sum([(1.0 - op) ** 2 for op in operands]) / len(operands))

def evaluate_or_operator(operands):
    return math.sqrt(sum([op ** 2 for op in operands]) / len(operands))

def evaluate_query(query, terms):#Aqui la query ya tiene que entrar en dfn
    all_query = query.split()
    index = 0
    for i in range(len(all_query)): #aqui pongo los terminos a que coincidan por como estan en el diccionario
        if(all_query[i] != "(" and all_query[i] != ")" and all_query[i] != "&" and all_query[i] != "|" and all_query[i] != "~"):
            all_query[i] = terms[index]
            index+=1
    result = ''
    for tup in all_query:
        result += tup + ' '
    temp = result.split('|')
    for i in range(len(temp)):
        print(i,"terminos a arreglassssssssssssssss")
        temp[i] = temp[i].replace('(', '')
        temp[i] = temp[i].replace(')', '')
        temp[i] = temp[i].replace('&', '')
        temp[i] = temp[i].replace('|', '')
    print(temp,"query finalllllllllllllllllllllllllllllllllllll")
    return temp    
       


    