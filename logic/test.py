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
import numpy as np

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
        doc_id = item[0].replace(
            'C:/Users/acer/Downloads/Telegram Desktop/vaswani/vaswani/', '')
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


def unpack():
    count = 0
    for doc in dataset.docs_iter():
        temp = open("C:/Users/acer/Downloads/Telegram Desktop/cord19trec_covidround1/" +
                    doc[0] + ".txt", 'w', encoding='utf-8', errors='replace')
        temp.write((doc[1]))
        temp.close()
        count += 1


# unpack()
def eval_models_and_draw():
    run = eval_model("vectorial")
    results = []
    c = 0
    # print(SetR.calc_aggregate(qrels, run))
    for x in ir_measures.iter_calc([P@5, R@5, SetF], qrels, run):
        results.append(x)
    # for x in ir_measures.iter_calc([P, R, SetF], qrels, run):

    measures = build_graphicss(results)
    draw_P(29, measures)
    draw_R(29, measures)
    draw_setF(29, measures)
    print("++++++++++++++++++++++++++++++++++++++++++++")

    print(np.mean(measures['P']))
    print(np.mean(measures['R']))
    print(np.mean(measures['SetF']))

    print(np.var(measures['P']))
    print(np.var(measures['R']))
    print(np.var(measures['SetF']))

    print("--------------------")