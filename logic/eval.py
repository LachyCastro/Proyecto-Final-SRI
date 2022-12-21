import matplotlib.pyplot as plt


def build_graphicss(results):
    p = []
    r = []
    setf = []
    for i, _ in enumerate(results):
        if i % 3 == 0:
            p.append(results[i].value)
        if i % 3 == 1:
            r.append(results[i].value)
        if i % 3 == 2:
            setf.append(results[i].value)
    measures = {'P': p, 'R': r, 'SetF': setf}
    return measures


def draw_P(num_querys, measures):
    # plt.figure(figsize=(15, 7))
    fig, ax = plt.subplots()
    querys = [i for i in range(num_querys + 1)]
    ax.plot(querys, measures['P'], color='tab:purple')
    plt.title("Precisión")
    plt.xlabel('Querys')
    plt.ylabel('Value')
    plt.show()


def draw_R(num_querys, measures):
    # plt.figure(figsize=(15, 7))
    fig, ax = plt.subplots()
    querys = [i for i in range(num_querys + 1)]
    ax.plot(querys, measures['R'], color='tab:purple')
    plt.title("Recobrado")
    plt.xlabel('Querys')
    plt.ylabel('Value')
    plt.show()


def draw_setF(num_querys, measures):
    # plt.figure(figsize=(15, 7))
    fig, ax = plt.subplots()
    querys = [i for i in range(num_querys + 1)]
    ax.plot(querys, measures['SetF'], color='tab:purple')
    plt.title("Medida F")
    plt.xlabel('Querys')
    plt.ylabel('Value')
    plt.show()