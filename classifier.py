import Levenshtein 

class Classifier:

    municipio = []
    departamento = []
    categoria = []

    def __init__(self):
        self.municipio = []
        self.departamento = []
        self.categoria = []

        with open('municipios.txt') as munf:
            self.municipio = munf.readlines()
        with open('departamentos.txt') as depf:
            self.departamento = depf.readlines()
        with open('categorias.txt') as catf:
            self.categoria = catf.readlines()


        self.municipio = [x.upper().strip() for x in self.municipio]
        self.departamento = [x.upper().strip() for x in self.departamento]
        self.categoria = [x.upper().strip() for x in self.categoria]

    def byMunicipio(self, value):
        minratio = 0
        rvalue = value
        c = 0
        for x in self.municipio:
            val = Levenshtein.ratio(value,x)
            if (val > minratio):
                rvalue = x
                minratio = value
            if (val == 1):
                return x
        return rvalue

    def byDepartamento(self, value):
        minratio = 0
        rvalue = value
        c = 0
        for x in self.departamento:
            val = Levenshtein.ratio(value,x)
            if (val > minratio):
                rvalue = x
                minratio = value
            if (val == 1):
                return x
        return rvalue

    def byCategoria(self, value):
        minratio = 0
        rvalue = value
        c = 0
        for x in self.categoria:
            val = Levenshtein.ratio(value,x)
            if (val > minratio):
                rvalue = x
                minratio = value
            if (val == 1):
                return x
        return rvalue
