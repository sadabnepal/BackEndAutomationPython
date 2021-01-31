import csv

with open('utilities/Loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile,delimiter=',')
    # print(list(csvReader))
    names = []
    stats = []
    for row in csvReader:
        names.append(row[0])
        stats.append(row[1])


print(names)
print(stats)

Index = names.index('Saqib')
print("Loan status is: ",stats[Index])

with open('utilities/Loanapp.csv', 'a') as writeFile:
    write = csv.writer(writeFile)
    write.writerow(['Domenic', 'Rejected'])

print(csvReader)