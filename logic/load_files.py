import os



def load_corpus(path):
    text = []
    dict_doc_path = {}
    #por ahora el metodo solo devolvera la lista de los documentos leidos
    if os.path.isdir(path):
        doc = 0
        for root, dirs, files in os.walk(path):
            for filename in files:
                with open(os.path.join(root,filename), encoding='utf8', errors='ignore') as f:
                    dict_doc_path[doc] = os.path.join(root,filename) 
                    doc+=1
                    text.append(f.read())
    else:
        #Exception("Direccion incorrecta")
        print("La direccion no es correcta")
    
    return [text, dict_doc_path]


#load_corpus('C:/Users/acer/Downloads/Telegram Desktop/SRI/corpus/alt.atheism/')