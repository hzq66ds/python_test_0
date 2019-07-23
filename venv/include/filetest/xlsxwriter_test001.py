import xlsxwriter


def filedeal():
    workbook = xlsxwriter.Workbook('xlsxtest001.xlsx')
    sheet = workbook.add_worksheet('sheet1')
    expenses = (
        ['Rent', 1000],
        ['Gas', 100],
        ['Food', 300],
        ['Gym', 50],
    )
    row = 0
    col = 0
    for key1, value1 in expenses:
        sheet.write(row, col, key1)
        sheet.write(row, col + 1, value1)
        row += 1
    sheet.write(row, 0, 'Total')
    sheet.write(row, 1, '=SUM(B1:B4)')
    workbook.close()
    print('filedeal_finish')


def filedeal01():
    with xlsxwriter.Workbook('xlsxtest002.xlsx') as workbook:
        sheet = workbook.add_worksheet('sheet1')

        expenses = (
            ['Rent', 1000],
            ['Gas', 100],
            ['Food', 300],
            ['Gym', 50],
        )
        row = 0
        col = 0
        for key1, value1 in expenses:
            sheet.write(row, col, key1)
            sheet.write(row, col + 1, value1)
            row += 1
        sheet.write(row, 0, 'Total')
        sheet.write(row, 1, '=SUM(B1:B4)')
        print('filedeal01_finish')


if __name__ == '__main__':
    filedeal()
    filedeal01()

#
write(row, column, token, [format])

