import csv
import requests
# 假设CSV文件名为'data.csv'
max = 140
min = 137
csv_filename = 'gmbz_docs1.csv'

# 创建一个字典来存储索引和文件信息的pair
file_info_dict = {}

# 打开CSV文件并读取内容
with open(csv_filename, mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # 如果有标题行，跳过它
    for row in reader:
        if len(row) >= 8:  # 确保行中有足够的数据
            index = row[0]  # 第1列是索引
            file_name_part1 = row[1]  # 第2列是文件名第一部分
            
            file_name_part2 = row[2]  # 第3列是文件名第二部分
            download_url = row[7]  # 第8列是下载地址

            # 组合文件名
            file_name = f"{file_name_part1}_{file_name_part2}"
            file_name = "{}.pdf".format(file_name.replace("/", ""))
            file_name = "{}".format(file_name.replace(":", "_"))

            # 将组合的文件名和下载地址作为一个pair存储在字典中
            file_info_dict[index] = (file_name, download_url)

# 打印结果，查看字典内容
for index, (file_name, download_url) in file_info_dict.items():
    # print(f"Index: {index}, File Name: {file_name}, Download URL: {download_url}")
    if(int(index) >= min and int(index) <= max):
        print(file_name)
        response = requests.get(download_url)
        with open(file_name, 'wb') as f:
            f.write(response.content)