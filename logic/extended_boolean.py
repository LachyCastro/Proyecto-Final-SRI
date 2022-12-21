# from .proc_text import *
from proc_text import *
import math
from sympy.logic.boolalg import to_dnf
from utils import terms_query
# from .utils import terms_query


def extended_ranking(dic_doc_words, vocabu, query, dic_doc_ind_tfidf):
    ranking = []
    for doc in dic_doc_words.keys():
        operands_for_or = []
        for component in query:
            operands_for_and = []
            x = component.split()
            for term in x:
                if (term in dic_doc_words[doc]) and (term in vocabu.keys()):
                    index_term = vocabu[term]
                    operands_for_and.append(
                        dic_doc_ind_tfidf[(doc, index_term)])
                else:
                    operands_for_and.append(0)
            if len(x) > 1:
                operands_for_or.append(evaluate_and_operator(operands_for_and))
            else:
                operands_for_or.append(operands_for_and[0])
        ranking.append(evaluate_or_operator(operands_for_or))
    return ranking


def evaluate_and_operator(operands):
    return 1.0 - math.sqrt(sum([(1.0 - op) ** 2 for op in operands]) / len(operands))


def evaluate_or_operator(operands):
    return math.sqrt(sum([op ** 2 for op in operands]) / len(operands))


def evaluate_query(query):  # Aqui la query ya tiene que entrar en dfn
    temp = query.split('|')
    result = []
    for i in range(len(temp)):
        component = ""
        temp[i] = terms_query(temp[i])
        for tup in temp[i]:
            component += tup + ' '
        result.append(component)
    return result
