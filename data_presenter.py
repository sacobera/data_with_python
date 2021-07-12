open_file = open('CupcakeInvoices.csv')

for row in open_file:
    #  print(row)
  for row in open_file:
    values =  row.split(',')
    # print(values[2])

    for row in open_file:
            values =  row.split(',')
            total = int(values[3]) * round(float(values[4]))
            print(total)
            
            for row in open_file:
                values =  row.split(',')
                total =  total + (int(values[3]) * float(values[4]))
            print(total)

open_file.close()


