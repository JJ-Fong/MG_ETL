from classifier import *
from datetime import datetime

class mySanitizer:
        
    def clean(self, value, dtype, fname):
        if (value.upper().strip() == 'NULL'):
            return 'null'
        if (dtype == "DATE"):
            value = self.dateformat(value)
            return value 
        elif (dtype == "TXT"):
            value = self.textformat(value) 
            return value
        elif (dtype == "NMB"):
            value = self.numberformat(value) 
            return value
        elif ((dtype == "GEO") or (dtype == "CATEGORY")):
            value = self.classify(value, fname)
        return value

    def dateformat(self, value):
        value = value.upper()
        value = value.replace(" ","")
        if 'HORA' in value:
            value = value[:value.index('HORA')]
        date = value.split('.')
        date = [x for x in date if (x != '')]

        try:
            if date[1].startswith('ENE'):
                date[1] = '01'
            elif date[1].startswith('FEB'):
                date[1] = '02'
            elif date[1].startswith('MAR'):
                date[1] = '03'
            elif date[1].startswith('ABR'):
                date[1] = '04'
            elif date[1].startswith('MAY'):
                date[1] = '05'
            elif date[1].startswith('JUN'):
                date[1] = '06'
            elif date[1].startswith('JUL'):
                date[1] = '07'
            elif date[1].startswith('AGO'):
                date[1] = '08'
            elif date[1].startswith('SEP'):
                date[1] = '09'
            elif date[1].startswith('OCT'):
                date[1] = '10'
            elif date[1].startswith('NOV'):
                date[1] = '11'
            elif date[1].startswith('DIC'):
                date[1] = '12'
        except:
            print value
            print date
            return 'null' 
        datestr = date[0]+date[1]+date[2]
        return datetime.strptime(datestr, '%d%m%Y')

    def textformat(self, value):
        value = value.decode('utf-8')
        value = value.upper().strip()
        value = value.replace("\"","") 
        return value

    def numberformat(self, value):
        try:
            value = value.replace("Q","")
            value = value.replace(",","")
            nvalue = float(value)
            return nvalue
        except:
            return value

    def classify(self, value, fieldName):
        classifier = Classifier() 
        value = value.upper().strip()
        fieldName = fieldName.upper().strip()
        minratio = 0
        rvalue = value
        if (fieldName == 'DEPARTAMENTO'):
            rvalue = classifier.byDepartamento(value)
        elif (fieldName == 'MUNICIPIO'):
            rvalue = classifier.byMunicipio(value)
        elif (fieldName == 'CATEGORIA'):
            rvalue = classifier.byCategoria(value)
        return rvalue
