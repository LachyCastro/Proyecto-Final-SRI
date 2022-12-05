from .proc_text import *

def valid_documents(dic_doc_words, dic_doc_patch, query):
    terms = terms_query(query)
    ranking = []
    index = 0
    query = rest_query(query, terms)
    print(query,"Queryyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
    for doc in dic_doc_words.keys():
        values = query
        for term in terms:
            if term in dic_doc_words[doc]:# el termino de la query esta en el documneto
                values = values.replace(term, 'True')
            else:
                values = values.replace(term, 'False')
        if(eval(values)):
            ranking.append(dic_doc_patch[index])
        index+=1
    return ranking

def terms_query(query):
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

def rest_query(query, terms): 
    all_query =  query.split()
    index = 0
    for i in range(len(all_query)):
        if(all_query[i] != "(" and all_query[i] != ")" and all_query[i] != "and" and all_query[i] != "or" and all_query[i] != "not"):
            all_query[i] = terms[index]
            index+=1
    result = ''
    for tup in all_query:
        result += tup + ' '
    return result


