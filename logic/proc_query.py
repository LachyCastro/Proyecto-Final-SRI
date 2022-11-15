from .proc_text import filter_words

def get_query_input(str_q):
    proc_query = []
    proc_query = filter_words(str_q).split()
    print(proc_query,"--------------")
    return proc_query




