import csv

with open('test.csv', 'w', newline='', encoding='utf-8') as wf:
    # 用csv文件包装
    writer = csv.writer(wf)

    # 创建头文件
    headers = ['Source', 'Target', 'Weight']
    writer.writerow(headers)

    # 写入数据
    lists = ['a', 'b', 'c']
    writer.writerow(lists)
    writer.writerow(['a', 'b', 'c'])
    writer.writerow(['a', 'b', 'c'])
    writer.writerow(['a', 'b', 'c'])
    # 一共写入4行数据

# newline='' 每一行的数据没有多余的空格
# encoding='utf-8' 文件编码格式是'utf-8'
