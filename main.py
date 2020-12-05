import camelot
import numpy
import pandas
import operator


tables = camelot.read_pdf('notas.pdf',pages='1-end')
print("Total tables extracted:", tables.n)

for x in range(len(tables)):
    print(tables[x].parsing_report)


a= numpy.vstack((tables[1].df,tables[2].df,tables[3].df))

print(a)

sorted_a = sorted(a,key=lambda x: x[6], reverse=True)

print(sorted_a)
pandas.DataFrame(sorted_a).to_csv("ola.csv")