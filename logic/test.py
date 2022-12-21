from utils import terms_query
from extended_boolean import evaluate_query
import ir_datasets
from ir_measures import *
import ir_measures
from main import vectorial_model, extended_boolean_model
from proc_query import get_query_input
import sys
import os
from eval import *
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

dataset = ir_datasets.load("vaswani")
qrels = dataset.qrels_iter()


def eval_model(name_model):
    run = {}
    results = []
    count = 0
    for query in dataset.queries_iter():
        procc_query = get_query_input(query[1])
        if name_model == 'extended_boolean':
            terms = terms_query(query[1])
            boolean_query = convert_boolean(procc_query)
            final_query = evaluate_query(boolean_query)
            results = extended_boolean_model(final_query, True)
        elif name_model == 'vectorial':
            results = vectorial_model(query[1])
        create_run(results, query, run)
        count += 1
        print(count)
    return run


def create_run(results, query, run):
    run[query[0]] = {}
    for item in results:
        doc_id = item[0].replace('C:/Users/lachy/Desktop/CRAN/vaswani\\', '')
        doc_id = doc_id.replace('.txt', '')
        if item[1] > 0.1:
            run[query[0]][doc_id] = item[1]


def convert_boolean(procc_query):
    query = " "
    for i in range(len(procc_query)):
        if i != len(procc_query)-1:
            query += ' ' + procc_query[i] + ' ' + '&'
        else:
            query += ' ' + procc_query[i]

    return query


# unpack()
run = eval_model("extended_boolean")
results = []
c = 0
for x in ir_measures.iter_calc([AP, SetF, SetR], qrels, run):
    c += 1
    results.append(x)

ap, setr, setf = build_graphicss(results)
draw(ap, setr, setf, 92)

print("++++++++++++++++++++++++++++++++++++++++++++")
