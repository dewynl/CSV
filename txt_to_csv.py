import csv

tabla = []

with open('respuestas.csv', 'r') as csv_respuestas:
    reader = csv.reader(csv_respuestas)
    for row in reader:
        l = []
        for column in row:
            l.append(column)
        tabla.append(l)
csv_respuestas.close()

new_table = []
#dewyn
#marcano
#gleyder

l = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
for i in range(len(tabla[0])):
    l = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    for j in range(3):
        if tabla[j][i] == 'Angustia':
            l[j][0] += 1
        elif tabla[j][i] == 'Alegria':
            l[j][1] += 1
        elif tabla[j][i] == 'Sorpresa':
            l[j][2] += 1
        elif tabla[j][i] == 'Disgusto':
            l[j][3] += 1
        elif tabla[j][i] == 'Neutral':
            l[j][4] += 1
    new_table.append(l)

final_table = []
for row in new_table:
    l = [0, 0, 0, 0, 0]
    for k in range(5):
        l[k] = row[0][k] + row[1][k] + row[2][k]
    final_table.append(l)

for line in final_table:
    print(line)

#Angustia, Alegria, Sorpresa, Disgusto, Neutral
with open('dataset.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Angustia', 'Alegria', 'Sorpresa', 'Disgusto', 'Neutral'])

    for index in range(len(final_table)):
        filewriter.writerow([final_table[index][0], final_table[index][1], final_table[index][2],
                             final_table[index][3], final_table[index][4]])
csvfile.close()




