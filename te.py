import Levenshtein

rh = 'RIO HONDO'

print Levenshtein.ratio(rh,'San Pedro Carch�'.upper())
print Levenshtein.ratio(rh,'R�o Hondo'.upper())
