#pip install openpyxl
from openpyxl import load_workbook
from openpyxl.styles import colors, Font, Fill, NamedStyle
from openpyxl.styles import PatternFill, Border, Side, Alignment

# 加载文件
wb = load_workbook('/Users/hanzhiqiang/Desktop/test.xlsx')

#wb.remove_sheet(new_sheet)
print("sheetnames:\t%s" % wb.sheetnames)
#for i in wb.sheetnames:
#    wb[i].title = '5a_'
for i in wb.sheetnames:
    print(i, "---------------------------行数%d\t烈数%d" % (wb[i].max_row, wb[i].max_column))
    for i1 in range(wb[i].max_row):
        for i2 in range(wb[i].max_column):
            print(wb[i].cell(i1+1, i2+1).value, end="\t")
        print("\n")


new_sheet = wb.create_sheet("new_sheet", 7)
new_sheet.sheet_properties.tabColor = "FFA500"
new_sheet.insert_rows(1)
new_sheet.insert_cols(2, 4)
