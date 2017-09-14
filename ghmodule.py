import Levenshtein
from datetime import datetime

geovalues = ['COB\xc3\xa1N', 'SAN PEDRO CARCH\xc3\xa1', 'SAN JUAN CHAMELCO', 'SAN CRIST\xc3\xb3BAL VERAPAZ', 'TACTIC', 'TUCUR\xc3\x9a', 'TAMAH\xc3\x9a', 'PANZ\xc3\xb3S', 'SENAH\xc3\x9a', 'CAHAB\xc3\xb3N', 'LANQU\xc3\xadN', 'CHAHAL', 'FRAY BARTOLOM\xc3\xa9 DE LAS CASAS', 'CHISEC', 'SANTA CRUZ VERAPAZ', 'SANTA CATALINA LA TINTA', 'RAXRUH\xc3\xa1', 'CUBULCO', 'SANTA CRUZ EL CHOL', 'GRANADOS', 'PURULH\xc3\xa1', 'RABINAL', 'SALAM\xc3\xa1', 'SAN MIGUEL CHICAJ', 'SAN JER\xc3\xb3NIMO', 'CHIQUIMULA', 'CAMOT\xc3\xa1N', 'CONCEPCI\xc3\xb3N LAS MINAS', 'ESQUIPULAS', 'IPALA', 'JOCOT\xc3\xa1N', 'OLOPA', 'QUEZALTEPEQUE', 'SAN JOS\xc3\xa9 LA ARADA', 'SAN JUAN ERMITA', 'SAN JACINTO', 'FLORES', 'DOLORES', 'LA LIBERTAD', 'LAS CRUCES', 'MELCHOR DE MENCOS', 'POPT\xc3\x9aN', 'SAN ANDR\xc3\xa9S', 'SAN BENITO', 'SAN FRANCISCO', 'SAN JOS\xc3\xa9', 'SAN LUIS', 'SANTA ANA', 'SAYAXCH\xc3\xa9', 'GUASTATOYA', 'MORAZ\xc3\xa1N', 'SAN AGUST\xc3\xadN ACASAGUASTL\xc3\xa1N', 'SAN CRIST\xc3\xb3BAL ACASAGUASTL\xc3\xa1N', 'EL J\xc3\xadCARO', 'SANSARE - SANARATE', 'SAN ANTONIO LA PAZ', 'SANTA CRUZ DEL QUICH\xc3\xa9', 'CANILL\xc3\xa1', 'CHAJUL', 'CHICAM\xc3\xa1N', 'CHICH\xc3\xa9', 'CHICHICASTENANGO', 'CHINIQUE', 'CUN\xc3\xa9N', 'IXC\xc3\xa1N', 'JOYABAJ', 'NEBAJ', 'PACHALUM', 'PATZIT\xc3\xa9', 'SACAPULAS', 'SAN ANDR\xc3\xa9S SAJCABAJ\xc3\xa1', 'SAN ANTONIO ILOTENANGO', 'SAN BARTOLOM\xc3\xa9 JOCOTENANGO', 'SAN JUAN COTZAL', 'SAN PEDRO JOCOPILAS', 'USPANT\xc3\xa1N', 'ZACUALPA', 'ESCUINTLA', 'GUANAGAZAPA', 'IZTAPA', 'LA DEMOCRACIA', 'LA GOMERA', 'TIQUISATE', 'MASAGUA', 'PAL\xc3\xadN', 'SAN JOS\xc3\xa9', 'SAN VICENTE PACAYA', 'SANTA LUC\xc3\xadA COTZUMALGUAPA', 'SIQUINAL\xc3\xa1', 'NUEVA CONCEPCI\xc3\xb3N', 'GUATEMALA CIUDAD', 'SANTA CATARINA PINULA', 'SAN JOS\xc3\xa9 PINULA', 'SAN JOS\xc3\xa9 DEL GOLFO', 'PALENCIA', 'CHINAUTLA', 'SAN PEDRO AYAMPUC', 'MIXCO', 'SAN PEDRO SACATEP\xc3\xa9QUEZ', 'SAN JUAN SACATEP\xc3\xa9QUEZ', 'SAN RAYMUNDO', 'CHUARRANCHO', 'FRAIJANES', 'AMATITL\xc3\xa1N', 'VILLA NUEVA', 'VILLA CANALES', 'SAN MIGUEL PETAPA', 'AGUACAT\xc3\xa1N', 'CHIANTLA', 'COLOTENANGO', 'CONCEPCI\xc3\xb3N HUISTA', 'CUILCO', 'HUEHUETENANGO', 'JACALTENANGO', 'LA DEMOCRACIA', 'LA LIBERTAD', 'MALACATANCITO', 'NENT\xc3\xb3N', 'SAN ANTONIO HUISTA', 'SAN GASPAR IXCHIL', 'SAN ILDEFONSO IXTAHUAC\xc3\xa1N', 'SAN JUAN ATIT\xc3\xa1N', 'SAN JUAN IXCOY', 'SAN MATEO IXTAT\xc3\xa1N', 'SAN MIGUEL ACAT\xc3\xa1N', 'SAN PEDRO NECTA', 'SAN PEDRO SOLOMA', 'SAN RAFAEL LA INDEPENDENCIA', 'SAN RAFAEL PETZA', 'SAN SEBASTI\xc3\xa1N COAT\xc3\xa1N', 'SAN SEBASTI\xc3\xa1N HUEHUETENANGO', 'SANTA ANA HUISTA.', 'SANTA B\xc3\xa1RBARA', 'SANTA CRUZ BARILLAS', 'SANTA EULALIA', 'SANTIAGO CHIMALTENANGO', 'TECTIT\xc3\xa1N', 'TODOS SANTOS CUCHUMAT\xc3\xa1N', 'UNI\xc3\xb3N CANTINIL', 'PUERTO BARRIOS', 'LIVINGSTON', 'EL ESTOR', 'MORALES', 'LOS AMATES', 'JALAPA', 'SAN PEDRO PINULA', 'SAN LUIS JILOTEPEQUE', 'SAN MANUEL CHAPARR\xc3\xb3N', 'SAN CARLOS ALZATATE', 'MONJAS', 'MATAQUESCUINTLA', 'JUTIAPA', 'AGUA BLANCA', 'ASUNCI\xc3\xb3N MITA', 'ATESCATEMPA', 'COMAPA', 'CONGUACO', 'EL ADELANTO', 'EL PROGRESO', 'JALPATAGUA', 'JEREZ', 'MOYUTA', 'QUESADA', 'SANTA CATARINA MITA', 'YUPILTEPEQUE', 'ZAPOTITL\xc3\xa1N', 'ALMOLONGA', 'CABRIC\xc3\xa1N', 'CAJOL\xc3\xa1', 'CANTEL', 'COATEPEQUE', 'COLOMBA', 'CONCEPCI\xc3\xb3N CHIQUIRICHAPA', 'EL PALMAR', 'FLORES COSTA CUCA', 'G\xc3\xa9NOVA', 'HUIT\xc3\xa1N', 'LA ESPERANZA', 'OLINTEPEQUE', 'SAN JUAN OSTUNCALCO', 'PALESTINA DE LOS ALTOS', 'QUETZALTENANGO', 'SALCAJ\xc3\xa1', 'SAN CARLOS SIJA', 'SAN FRANCISCO LA UNI\xc3\xb3N', 'SAN MART\xc3\xadN SACATEP\xc3\xa9QUEZ', 'SAN MATEO', 'SAN MIGUEL SIG\xc3\xbcIL\xc3\xa1', 'SIBILIA', 'ZUNIL', 'CHAMPERICO', 'EL ASINTAL', 'NUEVO SAN CARLOS', 'RETALHULEU', 'SAN ANDR\xc3\xa9S VILLA SECA', 'SAN MART\xc3\xadN ZAPOTITL\xc3\xa1N', 'SAN FELIPE', 'SAN SEBASTI\xc3\xa1N', 'SANTA CRUZ MULU\xc3\xa1', 'ALOTENANGO', 'ANTIGUA GUATEMALA', 'CIUDAD VIEJA', 'JOCOTENANGO', 'MAGDALENA MILPAS ALTAS', 'PASTORES', 'SAN ANTONIO AGUAS CALIENTES', 'SAN BARTOLOM\xc3\xa9 MILPAS ALTAS', 'SAN LUCAS SACATEP\xc3\xa9QUEZ', 'SAN MIGUEL DUE\xc3\xb1AS', 'SANTA CATARINA BARAHONA', 'SANTA LUC\xc3\xadA MILPAS ALTAS', 'SANTA MAR\xc3\xadA DE JES\xc3\x9aS', 'SANTIAGO SACATEP\xc3\xa9QUEZ', 'SANTO DOMINGO XENACOJ', 'SUMPANGO', 'SAN MARCOS', 'AYUTLA', 'CATARINA', 'COMITANCILLO', 'CONCEPCI\xc3\xb3N TUTUAPA', 'EL QUETZAL', 'EL RODEO', 'EL TUMBADOR', 'IXCHIGU\xc3\xa1N', 'LA REFORMA', 'MALACAT\xc3\xa1N', 'NUEVO PROGRESO', 'OC\xc3\xb3S', 'PAJAPITA', 'ESQUIPULAS PALO GORDO', 'SAN ANTONIO SACATEP\xc3\xa9QUEZ', 'SAN CRIST\xc3\xb3BAL CUCHO', 'SAN JOS\xc3\xa9 OJETENAM', 'SAN LORENZO', 'SAN MIGUEL IXTAHUAC\xc3\xa1N', 'SAN PABLO', 'SAN PEDRO SACATEP\xc3\xa9QUEZ', 'SAN RAFAEL PIE DE LA CUESTA', 'SIBINAL', 'SIPACAPA', 'TACAN\xc3\xa1', 'TAJUMULCO', 'TEJUTLA', 'R\xc3\xadO BLANCO', 'CUILAPA', 'BARBERENA', 'CASILLAS', 'CHIQUIMULILLA', 'GUAZACAP\xc3\xa1N', 'NUEVA SANTA ROSA', 'ORATORIO', 'PUEBLO NUEVO VI\xc3\xb1AS', 'SAN JUAN TECUACO', 'SAN RAFAEL LAS FLORES', 'SANTA CRUZ NARANJO', 'SANTA MAR\xc3\xadA IXHUAT\xc3\xa1N', 'SANTA ROSA DE LIMA', 'TAXISCO', 'SOLOL\xc3\xa1', 'CONCEPCI\xc3\xb3N', 'NAHUAL\xc3\xa1', 'PANAJACHEL', 'SAN ANDR\xc3\xa9S SEMETABAJ', 'SAN ANTONIO PALOP\xc3\xb3', 'SAN JOS\xc3\xa9 CHACAY\xc3\xa1', 'SAN JUAN LA LAGUNA', 'SAN LUCAS TOLIM\xc3\xa1N', 'SAN MARCOS LA LAGUNA', 'SAN PABLO LA LAGUNA', 'SAN PEDRO LA LAGUNA', 'SANTA CATARINA IXTAHUAC\xc3\xa1N', 'SANTA CATARINA PALOP\xc3\xb3', 'SANTA CLARA LA LAGUNA', 'SANTA CRUZ LA LAGUNA', 'SANTA LUC\xc3\xadA UTATL\xc3\xa1N', 'SANTA MAR\xc3\xadA VISITACI\xc3\xb3N', 'SANTIAGO ATITL\xc3\xa1N', 'MAZATENANGO', 'CHICACAO', 'CUYOTENANGO', 'PATULUL', 'PUEBLO NUEVO', 'R\xc3\xadO BRAVO', 'SAMAYAC', 'SAN ANTONIO SUCHITEP\xc3\xa9QUEZ', 'SAN BERNARDINO', 'SAN JOS\xc3\xa9 EL \xc3\x8dDOLO', 'SAN FRANCISCO ZAPOTITL\xc3\xa1N', 'SAN GABRIEL', 'SAN JUAN BAUTISTA', 'SAN LORENZO', 'SAN MIGUEL PAN\xc3\xa1N', 'SAN PABLO JOCOPILAS', 'SANTA BARBARA', 'SANTO DOMINGO SUCHITEPEQUEZ', 'SANTO TOMAS LA UNI\xc3\xb3N', 'ZUNILITO', 'TOTONICAP\xc3\xa1N', 'MOMOSTENANGO', 'SAN ANDR\xc3\xa9S XECUL', 'SAN BARTOLO', 'SAN CRIST\xc3\xb3BAL TOTONICAP\xc3\xa1N', 'SAN FRANCISCO EL ALTO', 'SANTA LUC\xc3\xadA LA REFORMA', 'SANTA MAR\xc3\xadA CHIQUIMULA', 'CABA\xc3\xb1AS', 'ESTANZUELA', 'GUAL\xc3\xa1N', 'HUIT\xc3\xa9', 'LA UNI\xc3\xb3N', 'R\xc3\xadO HONDO', 'SAN DIEGO', 'TECULUT\xc3\xa1N', 'USUMATL\xc3\xa1N', 'ZACAPA', 'ACATENANGO', 'CHIMALTENANGO', 'EL TEJAR', 'PARRAMOS', 'PATZIC\xc3\xadA', 'PATZ\xc3\x9aN', 'POCHUTA', 'SAN ANDR\xc3\xa9S ITZAPA', 'SAN JOS\xc3\xa9 POAQU\xc3\xadL', 'SAN JUAN COMALAPA', 'SAN MART\xc3\xadN JILOTEPEQUE', 'SANTA APOLONIA', 'SANTA CRUZ BALANY\xc3\xa1', 'TECP\xc3\xa1N', 'YEPOCAPA', 'ZARAGOZA', 'ALTA VERAPAZ', 'BAJA VERAPAZ', 'CHIMALTENANGO', 'CHIQUIMULA', 'EL PROGRESO', 'ESCUINTLA', 'GUATEMALA', 'HUEHUETENANGO', 'IZABAL', 'JALAPA', 'JUTIAPA', 'PET\xc3\xa9N', 'QUETZALTENANGO', 'QUICH\xc3\xa9', 'RETALHULEU', 'SACATEP\xc3\xa9QUEZ', 'SAN MARCOS', 'SANTA ROSA', 'SOLOL\xc3\xa1', 'SUCHITEP\xc3\xa9QUEZ', 'TOTONICAP\xc3\xa1N', 'ZACAPA']

def clean(value, stype):
    if (value.upper().strip() == 'NULL'):
        return 'null'
    if (stype == "DATE"):
        value = dateformat(value)
        return value 
    elif (stype == "TXT"):
        value = textformat(value) 
        return value
    elif (stype == "NMB"):
        value = numberformat(value) 
        return value
    elif (stype == "GEO"):
        value = geoclassifier(value) 
        return value

def dateformat(value):
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
    
def textformat(value):
    value = value.decode('utf-8')
    value = value.upper().strip()
    return value

def numberformat(value):
    try:
        value = value.replace("Q","")
        value = value.replace(",","")
        nvalue = float(value)
        return nvalue
    except:
        return value

def geoclassifier(value):
    #value = value.decode('utf-8')
    value = value.upper().strip()
    minratio = 0
    rvalue = value
    c = 0
    for x in geovalues:
        val = Levenshtein.ratio(value, x)
        if (val > minratio):
            rvalue = x
            minratio = val
        if (val == 1):
            return x
    return rvalue
