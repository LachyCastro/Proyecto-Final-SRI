import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from logic.proc_query import get_query_input
from logic.main import vectorial_model, extended_boolean_model
import ir_measures
from ir_measures import *
import ir_datasets
from logic.extended_boolean import evaluate_query
from logic.utils import terms_query
dataset = ir_datasets.load("vaswani")
qrels = dataset.qrels_iter()

# def unpack():
#     count = 0
#     for doc in dataset.docs_iter():
#         temp = open("C:/Users/lachy/Desktop/CRAN/vaswani/" + doc[0] + ".txt",'w',encoding='utf-8', errors= 'replace')
#         temp.write((doc[1]))
#         temp.close()
#         count+=1
 
def eval_model(name_model):
    run = {}
    results = []
    count = 0 
    for query in dataset.queries_iter():
        procc_query = get_query_input(query[1])
        if name_model == 'extended_boolean':
            terms = terms_query(query[1])
            boolean_query = convert_boolean(procc_query)
            final_query = evaluate_query(boolean_query,terms)
            results = extended_boolean_model(final_query,True)
        elif name_model == 'vectorial':
            results = vectorial_model(query[1])   
        create_run(results,query,run)
        count+=1
        print(count)
    return run

def create_run(results,query,run):
    run[query[0]] ={}
    for item in results:
        doc_id = item[0].replace('C:/Users/lachy/Desktop/CRAN/vaswani\\','')
        doc_id = doc_id.replace('.txt', '')
        if item[1] > 0 :
            run[query[0]][doc_id] = item[1]
       

def convert_boolean(procc_query):
    query = " "
    for i in range(len(procc_query)):
        if i != len(procc_query)-1:
            query += ' ' + procc_query[i] + ' ' + '&'
        else:
            query += ' ' + procc_query[i]

    return query


#unpack()
run = eval_model("vectorial")    

print(AP.calc_aggregate(qrels,run))


# if __name__ == "__main__":

#     if len(sys.argv) == 4:
# dataset = ir_datasets.load("vaswani")
# qrels = dataset.qrels_iter()
# run = eval_model(sys.argv[1], sys.argv[2], sys.argv[3])
# eval = ir_measures.iter_calc([ SetP, SetP, SetF, SetF], qrels, run)
 
# for item in eval:
#     print(item)