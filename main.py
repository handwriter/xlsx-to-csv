import xlrd


rb = xlrd.open_workbook('data.xlsx')
sheet = rb.sheet_by_index(0)
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
with open('output.csv', 'w') as out:
    for i in vals:
        print(i)
        out.write(';'.join(list(map(str, i))) + '\n')