import re


def parser_cran(path):
    with open(path, 'r') as f:
        texts = f.read().split('\n.I')
    my_text = []
    for te in texts:
        temp = re.search(r'\n\.W(.*)', te)
        my_text.append(te[temp.regs[0][1]:])
    for i in range(len(my_text)):
        my_text[i] = my_text[i][1:]
    return my_text


def unpack_cran(text_list):
    for i in range(len(text_list)):
        temp = open("C:/Users/lachy/Desktop/CRAN/asd/" + str(i) + ".txt", 'w')
        temp.write(text_list[i])
        temp.close()


def parser_querys_cran(path):
    with open(path, 'r') as f:
        texts = f.read().split('\n.I')
    #    print(texts)
    my_querys = []
    for q in texts:
        temp = re.search(r'\n\.W(.*)', q)
        my_querys.append(q[temp.regs[0][1]:])
    for i in range(len(my_querys)):
        my_querys[i] = my_querys[i][1:]
    for i in range(len(my_querys)):
        my_querys[i] = my_querys[i].replace('\n', ' ')
    return my_querys
