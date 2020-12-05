import camelot
import numpy
import pandas


tables = camelot.read_pdf('notas.pdf',pages='1-end')
print("Total tables extracted:", tables.n)

for x in range(len(tables)):
    print(tables[x].parsing_report)

camelot.plot(tables[0], kind='text').show()
camelot.plot(tables[0], kind='line').show()
camelot.plot(tables[0], kind='contour').show()


a= numpy.vstack((tables[1].df,tables[2].df,tables[3].df))

print(a)


pandas.DataFrame(a).to_csv("ola.csv")