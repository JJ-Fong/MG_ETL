import Levenshtein 

class Classifier:

    municipio = []
    departamento = []
    categoria = []

    def __init__(self):
        self.municipio = []
        self.departamento = []
        self.categoria = []

        with open('Catalogs/municipios.txt') as munf:
            self.municipio = munf.readlines()
        with open('Catalogs/departamentos.txt') as depf:
            self.departamento = depf.readlines()
        with open('Catalogs/categorias.txt') as catf:
            self.categoria = catf.readlines()


        self.municipio = [x.decode('latin-1').upper().strip() for x in self.municipio]
        self.departamento = [x.decode('latin-1').upper().strip() for x in self.departamento]
        self.categoria = [x.decode('latin-1').upper().strip() for x in self.categoria]

    def byMunicipio(self, value):
        minratio = 0
        rvalue = value
        c = 0
        for x in self.municipio:
            val = Levenshtein.ratio(value,x.encode('utf-8'))
            if (val > minratio):
                rvalue = x.strip()
                minratio = val
            if (val == 1):
                return x.strip()
        return rvalue

    def byDepartamento(self, value):
        minratio = 0
        rvalue = value
        c = 0
        for x in self.departamento:
            val = Levenshtein.ratio(value,x.encode('utf-8'))
            if (val > minratio):
                rvalue = x.strip()
                minratio = val
            if (val == 1):
                return x.strip()
        return rvalue

    def byCategoria(self, value):
        minratio = 0
        rvalue = value
        c = 0
        for x in self.categoria:
            val = Levenshtein.ratio(value,x.encode('utf-8'))
            if (val > minratio):
                rvalue = x.strip()
                minratio = val
            if (val == 1):
                return x.strip()
        return rvalue
