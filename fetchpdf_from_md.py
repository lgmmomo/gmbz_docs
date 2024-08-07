import requests
from bs4 import BeautifulSoup

max = 119
min = 79

# max = 10
# min = 10
# 获取PDF文件的URL
url = "http://www.gmbz.org.cn/file/2018-01-17/74efb470-4bc5-4714-b5f6-655bf00fc702.pdf"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# pdf_link = soup.find('string', href=True, text="Download PDF")
# pdf_url = pdf_link['href']
# print(pdf_url)

# 假设Markdown表格文件名为'markdown_table.md'
file_name = 'README.md'

# 读取文件内容
with open(file_name, 'r', encoding='utf-8') as file:
    markdown_content = file.read()

# 用于存储结果的字典
gmbz_docs = {}

# 首先，移除markdown表格的头部
lines = markdown_content.split('\n')
header = lines[1]  # 表格头部
content_lines = lines[8:-1]  # 表格内容
# print(content_lines)
# 遍历每一行内容
for index, line in enumerate(content_lines, start=1):  # 从1开始计数
    # 移除行中的'|'和空格，然后分割
    parts = line.strip().split('|')
    # print(parts)
    # 合并行标号和标准中文名称
    standard_info = parts[2].strip() + ' ' + parts[3].strip()
    # pdf_filename = r"{}.pdf".format(standard_info)
    pdf_filename = "{}.pdf".format(standard_info.replace("/", ""))
    # print(standard_info)
    # 获取PDF下载链接
    pdf_url = parts[-2].strip()
    # print(pdf_url)
    # 存储到字典中，使用序号作为键
    gmbz_docs[index] = (pdf_filename, pdf_url)
    # print(gmbz_docs)
# # 输出结果
for idx, (info, url) in gmbz_docs.items():
    # print(f"Index: {idx}, Info: '{info}', URL: {url}")

# 下载PDF文件
    if(idx >= min and idx <= max):
        response = requests.get(url)
        with open(info, 'wb') as f:
            f.write(response.content)

# print("PDF文件下载完成！")