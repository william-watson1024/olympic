import json
from collections import defaultdict

# 定义输入文件名
input_filename = 'output.json'  # 请将此处替换为你的输入文件名

# 从文件中读取比赛数据
with open(input_filename, 'r', encoding='utf-8') as file:
    matches = json.load(file)

# 创建一个字典来分类存储比赛数据
grouped_matches = defaultdict(list)

# 将比赛数据按组别分类，排除包含“女子”的比赛
for match in matches:
    # 检查是否包含“女子”，若包含则跳过
    if "女子" in match["info"]:
        continue
    
    # 从比赛信息中提取组别
    group_info = match["info"].split(",")[0]  # 取出组别
    grouped_matches[group_info].append(match)

# 保存数据到不同的JSON文件
for group, content in grouped_matches.items():
    filename = f"{group}.json"
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(content, json_file, ensure_ascii=False, indent=4)

print("数据已保存到JSON文件中。")
