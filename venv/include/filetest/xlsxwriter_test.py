import xlsxwriter


if __name__ == '__main__':
    f = xlsxwriter.Workbook()
    worksheet1 = f.add_worksheet('操作日志')
    bold = f.add_format({
        'bold': True,  # 字体加粗
        'border': 1,  # 单元格边框宽度
        'align': 'left',  # 水平对齐方式
        'valign': 'vcenter',  # 垂直对齐方式
        'fg_color': '#F4B084',  # 单元格背景颜色
        'text_wrap': True,  # 是否自动换行
    })
    # row:行， col：列， data:要写入的数据, bold:单元格的样式
    worksheet1.write(row, col, data, bold)
    # A1:从A1单元格开始插入数据，按行插入， data:要写入的数据（格式为一个列表), bold:单元格的样式
    worksheet1.write_row('A1', data, bold)

    # A1:从A1单元格开始插入数据，按列插入， data:要写入的数据（格式为一个列表), bold:单元格的样式
    worksheet1.write_column('A1', data, bold)
    # 第一个参数是插入的起始单元格，第二个参数是图片你文件的绝对路径
    worksheet1.insert_image('A1', 'f:\\1.jpg')
    worksheet1.write_url(row, col, "internal:%s!A1" % '要关联的工作表表名', string="超链接显示的名字")
    workbook.add_chartsheet(type = "")

    #参数中的type指的是图表类型，图表类型示例如下：
    # [area：面积图, bar：条形图, column：直方图, doughnut：环状图, line：折线图, pie：饼状图, scatter：散点图, radar：雷达图, stock:箱线图]

    workbook.worksheets()
    # 关闭excel文件
    workbook.close()
