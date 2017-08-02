def clean(value, stype):
    if (stype == "DATE"):
        value = dateformat(value)
    elif (stype == "TXT"):
        value = textformat(value)
    elif (stype == "NMB"):
        value = numberformat(value)
    elif (stype == "GEO"):
        value = geoclassifier(value) 
    return value

def dateformat(value):
    return value

def textformat(value):
    return value

def numberformat(value):
    return value

def geoclassifier(value):
    return value
