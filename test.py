

with open('municipios.txt') as f:
    content = f.readlines()

content = [x.upper().strip() for x in content] 
rep = [] 
for mun in content:
    count = 0 
    for i in range(len(content)):
        if (content[i] == mun):
            count += 1
    if count > 1:
        print mun, count
