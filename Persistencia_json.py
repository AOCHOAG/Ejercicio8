import json
def store(var, filename):
    json.dump(json.dumps(var), open(filename, "w")) #Le estamos diciendo que almacene el valor de la variable en var
                                                    #Le decimos que lo escribamos en el archivo filename
def retrieve(filename):
    var = json.loads(json.load(open(filename, "r")))
    return var





