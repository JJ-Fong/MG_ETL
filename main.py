# coding=utf-8
import csv
import json
from collections import defaultdict
import ghmodule
from datetime import datetime
import uuid

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
    if (len(f["files"]) > 0):
        for field in schemas[f["schema"]]:
            fname, ftype = field
            fieldName.append(fname)
            fieldType.append(ftype)
        idn = ''
        if (f["schema"] == 'raw_proveedores'):
            idn = 'rp_'
        elif (f["schema"] == 'raw_compradores'):
            idn = 'rc_'
        elif (f["schema"] == 'raw_adjudicaciones'):
            idn = 'ra_'
        idn += uuid.uuid4().hex 
        for sfile in f["files"]:
            print sfile
            with open(sfile) as csvf:
                reader = csv.DictReader(csvf, delimiter='|')
                #Revisar que el CSV tiene la estructura correcta
                csvfn = reader.fieldnames
                #Esta linea debe ser removida cuando se corrijan los formatos de los csv
                csvfn = [x for x in csvfn if ((x != '')and(x != ','))]
                #La variable FLAG nos dice si la estructura del csv actual es igual a la esperada segun el esquema
                flag = (len(csvfn) == len(fieldName))
                i = 0
                while (flag and (i < len(fieldName))):
                    flag = (flag and (csvfn[i].upper() in fieldName))
                    i += 1
                #Empieza escritura de nuevo csv consolidado
                if (flag):
                    with open(str(idn)+'.csv', 'ab') as newfile:
                        wr = csv.writer(newfile, delimiter='|')
                        count = 0 
                        for row in reader:
                            rec = []
                            fc = 0
                                    #if ((f["schema"] == 'raw_adjudicaciones')):
                                            #print fn, row[fn], fieldType[fieldName.index(fn.upper())]
                                    #    print count
                                    #    print row
                            for fn in csvfn:
                                        
                                rec.append(ghmodule.clean(row[fn],fieldType[fieldName.index(fn.upper())]))
                                fc += 1
                                    
                                    #if ((f["schema"] == 'raw_adjudicaciones')and(count > 3070)):
                                    #    print count, sfile, rec

                            frec = []
                            for item in rec:
                                try:
                                    frec.append(item.encode('utf-8'))
                                except:
                                    frec.append(item) 
                            wr.writerow(frec)
                            count += 1
                            
