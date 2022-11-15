import os

from matplotlib.pyplot import title


titles = []
text = []

def load_corpus(path):
    #por ahora el metodo solo devolvera la lista de los documentos leidos
    if os.path.isdir(path):
        
        for root, dirs, files in os.walk(path):
            for filename in files:
                with open(os.path.join(root,filename), encoding='utf8', errors='ignore') as f:
                    titles.append(filename)
                    text.append(f.read())
    else:
        #Exception("Direccion incorrecta")
        print("La direccion no es correcta")

    return text

