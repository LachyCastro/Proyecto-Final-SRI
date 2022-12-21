import matplotlib.pyplot as plt


def build_graphicss(results):
    ap = []
    setr = []
    setf = []
    for i, _ in enumerate(results):
        if i % 3 == 0:
            ap.append(results[i].value)
        if i % 3 == 1:
            setr.append(results[i].value)
        if i % 3 == 2:
            setf.append(results[i].value)
    return ap, setr, setf


def draw(ap, setr, setf, num_querys):
    fig, ax = plt.subplots()
    querys = [i for i in range(num_querys + 1)]
    measures = {'AP': ap, 'SetR': setr, 'SetF': setf}
    ax.plot(querys, measures['AP'], color='tab:purple')
    ax.plot(querys, measures['SetR'], color='tab:green')
    ax.plot(querys, measures['SetF'], color='tab:cyan')
    plt.show()
