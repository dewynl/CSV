import csv_counter

columns = []
with open('noticias2.csv') as csvfile:
    reader = csv_counter.reader(csvfile)
    for row in reader:
        list = []
        for column in row:
           list.append(column)
        columns.append(list)


mayorias = columns[3]
angustia = 0
alegria = 0
sorpresa = 0
disgusto = 0
neutro = 0
nulo = 0

for i in range(len(mayorias)):
    if mayorias[i] == "Alegria":
        alegria += 1
    elif mayorias[i] == "Disgusto":
        disgusto += 1
    elif mayorias[i] == "Sorpresa":
        sorpresa += 1
    elif mayorias[i] == "Angustia":
        angustia += 1
    elif mayorias[i] == "Neutral":
        neutro += 1
    elif mayorias[i] == "Nulo":
        nulo += 1

print("Total noticias: " + str(angustia + alegria + sorpresa + disgusto + neutro + nulo))

print("Alegria: %s, Angustia: %s, Sopresa: %s, Disgusto: %s, Neutrales: %s, Nulas: %s " % (alegria, angustia, sorpresa, disgusto, neutro, nulo))

del columns[3]

total_acuerdo = 0
for i in range(len(columns[0])):
    if columns[0][i] == columns[1][i] and columns[1][i] == columns[2][i]:
        total_acuerdo += 1

print("Noticias con 100% de acuerdo: " + str(total_acuerdo))


