import json

# 读取 JSON 文件
with open('0811.json', 'r', encoding='utf-8') as infile:
    data = json.load(infile)

# 替换空竞争者数据
for event in data:
    if not event["competitors"]:
        event["competitors"] = [
            {
                "noc": "",
                "name": "",
                "mark": "",
                "winnerLoserTie": ""
            },
            {
                "noc": "",
                "name": "",
                "mark": "",
                "winnerLoserTie": ""
            }
        ]

# 输出结果到新的 JSON 文件
with open('0811.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)
