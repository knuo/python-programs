import xlrd
import matplotlib.pyplot as plt


workbook = xlrd.open_workbook("grap.xlsx")
first_sheet = workbook.sheet_by_index(0)

x = [first_sheet.cell_value(i, 0) for i in range(first_sheet.nrows)]
y = [first_sheet.cell_value(i, 1) for i in range(first_sheet.nrows)]

plt.plot(x,y)
plt.axis([0,6,0,36])
plt.show()