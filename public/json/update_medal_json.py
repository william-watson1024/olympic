import json
import os

with open('medal.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 更新每个国家的 flag 字段
for item in data:
    country_code = item['countryid']
    flag_path = f'./country_images/{country_code}.png'
    item['flag'] = flag_path

# 将更新后的数据写回 medal.json 文件
with open('medal.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("medal.json 文件已更新，添加了 flag 字段。")