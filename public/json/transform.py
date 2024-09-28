import json

def transform_match_data(source):
    # 提取必要数据
    specific_event = source.get("specificEvent")
    match_code = source.get("matchCode")
    competitors = source.get("competitors", [])  # 提供默认值为空列表
    date = source.get("date")
    start_date = source.get("startDate")

    # 构造 info 字段
    info = f"{specific_event}, 比赛{match_code}"

    # 检查 competitors 是否为列表并且不为空
    if competitors and isinstance(competitors, list):
        # 构造 teams 字段
        teams = [
            {
                "name": competitor.get("name"),
                "flag": competitor.get("noc"),
                "score": int(competitor.get("mark"))  # 确保分数是整数
            }
            for competitor in competitors
        ]
    else:
        teams = []  # 如果没有竞争者，返回空列表

    # 构造 time 字段
    time = f"{date['month']}月{date['day']}日 {start_date}"

    # 构造新的对象
    result = {
        "info": info,
        "teams": teams,
        "time": time,
        "status": "已结束"
    }

    return result

if __name__ == "__main__":
    input_file = '足球.json'  # 输入文件名
    output_file = 'output.json'  # 输出文件名

    # 从文件读取数据
    with open(input_file, 'r', encoding='utf-8') as infile:
        source_data = json.load(infile)

    transformed_data_list = []

    # 遍历 items 中的每个比赛数据
    for event in source_data:
        items = event.get("items", [])
        for match in items:
            transformed_data = transform_match_data(match)
            transformed_data_list.append(transformed_data)

    # 将结果写入输出文件
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(transformed_data_list, outfile, ensure_ascii=False, indent=2)

    print(f"转换后的数据已写入到 {output_file}")
