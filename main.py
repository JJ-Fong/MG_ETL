import csv
import json
from collections import defaultdict
import ghmodule

#Carga de JSON con los esquemas de los modelos crudos
with open('schemas.json') as schemasf:
    schemasj = json.load(schemasf)
#Carga de JSON con la informacion de los archivos a consolidar
with open('files.json') as filesf:
    files = json.load(filesf)

#Se ingresan los esquemas a un diccionario para su rapida lectura
schemas = defaultdict(list)
for sch in schemasj["tables"]:
    tname = sch["tablename"]
    for field in sch["fields"]:
        schemas[tname].append((field["name"],field["type"]))

#Manejo de CSV
for f in files["files"]:
    fieldName = []
    fieldType = []
    for field in schemas[f["schema"]]:
        fname, ftype = field
        fieldName.append(fname)
        fieldType.append(ftype)
    for sfile in f["files"]:
        with open(sfile) as csvf:
            reader = csv.DictReader(csvf, delimiter='|')
            #Revisar que el CSV tiene la estructura correcta
            csvfn = reader.fieldnames
            csvfn = [x for x in csvfn if ((x != '')and(x != ','))]
            flag = (len(csvfn) == len(fieldName))
            if (
            
