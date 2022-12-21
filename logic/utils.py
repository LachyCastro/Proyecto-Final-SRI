from .proc_text import *
#from proc_text import *


def bracket_verify(full_query):
    bracket_stack = []

    for word in full_query:
        if word == "(":
            bracket_stack.append("(")
        elif word == ")":
            if len(bracket_stack) > 0:
                bracket_stack.pop()
            else:
                raise Exception("unmatched ')'") 
    if len(bracket_stack) > 0:
        raise Exception("unmatched ')'")


def terms_query(query):  # Pasar a utils q esta repetido para el booleano extendido, estos son los terminos por donde iterar
    terms = query.replace('(', '')
    terms = terms.replace(')', '')
    terms = terms.replace('&', '')
    terms = terms.replace('|', '')
    terms = terms.replace('~', '')
    f1 = repleace_contractions(terms)
    f2 = stem_tokens(f1)
    f3 = repleace_punctuation_marks(f2)
    return f3
