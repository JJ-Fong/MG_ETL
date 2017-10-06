# coding=utf-8
import csv
import json
from sanitizer import *
import uuid
from collections import defaultdict
from datetime import datetime
import os.path


#Instancia del sanitizador
sanitizer = mySanitizer() 
file_path = 'C:\Users\Javier Fong\Documents\Universidad\CICLO 10\Megaproyecto\Repository\Consolidated Data'
#Carga de JSON con los esquemas de los modelos crudos
with open('json/schemas.json') as schemasf:
    schemasj = json.load(schemasf)
#Carga de JSON con la informacion de los archivos a consolidar
with open('json/files.json') as filesf:
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
                    file_name = os.path.join(file_path,idn)+".csv"
                    with open(file_name, 'ab') as newfile:
                        wr = csv.writer(newfile, delimiter='|')
                        #wr.writerow(fieldName)
                        count = 0 
                        for row in reader:
                            #registros a insertar
                            records = [[]]
                            for field in csvfn:
                                value = row[field]
                                value = value.split("~")
                                if (len(value)>1):
                                    nrecords = []
                                    for i in range(len(value)):     
                                        for j in range(len(records)):
                                            nrec = []
                                            for k in range(len(records[j])):
                                                nrec.append(records[j][k])
                                            nrecords.append(nrec)
                                    records = nrecords
                                fTypeIndex = fieldName.index(field.upper())
                                cv = 0
                                rosize = int(len(records)/len(value))    
                                for v in value:
                                    nv = sanitizer.clean(v, fieldType[fTypeIndex], field.upper())
                                    try:
                                        nv = nv.encode('utf-8')
                                    except:
                                        nv = nv
                                    for cc in range(rosize):
                                        records[(cv*rosize)+cc].append(nv) 
                                    cv += 1
                            for rec in records:
                                wr.writerow(rec)
                            count += 1
                            
                            
