import Levenshtein

rh = 'RIO HONDO'

print Levenshtein.ratio(rh,'San Pedro Carchá'.upper())
print Levenshtein.ratio(rh,'Río Hondo'.upper())
