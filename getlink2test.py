import requests
from bs4 import BeautifulSoup
import csv

# 初始页面URL
base_url = 'http://www.gmbz.org.cn/main/bzlb.html'

# 请求第一页内容
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# 存储所有数据的列表
all_data = []

# 解析表格数据
table = soup.find('table')
rows = table.find_all('tr')[1:]  # 跳过表头
for row in rows:
    cols = row.find_all('td')
    if cols:
        all_data.append([col.text.strip() for col in cols])

# 找到分页链接
pagination = soup.find('div', class_='pagination')  # 根据实际的HTML类名调整
pages = [a['href'] for a in pagination.find_all('a', href=True) if a.text.isdigit()]

# 如果有分页，循环遍历所有页面
for page in pages:
    # 请求分页内容
    page_url = base_url + page
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 解析当前页的表格数据并添加到all_data列表中
    table = soup.find('table')
    rows = table.find_all('tr')[1:]  # 跳过表头
    for row in rows:
        cols = row.find_all('td')
        if cols:
            all_data.append([col.text.strip() for col in cols])

# 写入CSV文件
csv_file = 'gmbz_standards.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # 写入表头
    writer.writerow(['行标号', '标准名称', '类别', '状态', '英文名称', '牵头单位', '合作单位', '发布', '实施', '上升国标', '操作'])
    # 写入所有数据
    writer.writerows(all_data)

print(f'数据已写入 {csv_file}')