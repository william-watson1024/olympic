import json
import os
from datetime import datetime, timedelta

# 定义文件路径
input_file = '0725.json'
output_file = '0725_output.json'

# 定义时区调整（+6 小时）
TIMEZONE_OFFSET = 6

# 提取数据的函数
def extract_data(data):
    result_list = []
    
    for unit in data.get("units", []):
        discipline_name = unit.get("disciplineName", "")
        event_unit_name = unit.get("eventUnitName", "")
        start_date = unit.get("startDate", "")
        adjusted_time = adjust_time(start_date)  # 调整时间

        # 创建 event 的基本信息
        event_info = {
            "disciplineName": discipline_name,
            "event": event_unit_name,  # 使用 eventUnitName
            "startDate": adjusted_time,
            "competitors": []
        }

        # 处理 "competitors" 数据
        for competitor in unit.get("competitors", []):
            noc = competitor.get("noc", "")
            name = competitor.get("name", "")
            results = competitor.get("results", {})
            mark = results.get("mark", "")
            winner_loser_tie = results.get("winnerLoserTie", "")

            # 转换 noc 为国旗图像路径格式
            noc_image_path = f"./country_images/{noc}.png" if noc else ""

            # 添加 competitor 数据
            event_info["competitors"].append({
                "noc": noc_image_path,  # 使用国旗图像路径代替 noc
                "name": name,
                "mark": mark,
                "winnerLoserTie": winner_loser_tie
            })
        
        # 将每个 event 的信息加入结果列表
        result_list.append(event_info)
    
    return result_list

# 时间调整函数
def adjust_time(start_date_str):
    try:
        # 将原始日期字符串转换为 datetime 对象
        original_time = datetime.strptime(start_date_str, "%Y-%m-%dT%H:%M:%S%z")
        
        # 将时间偏移 +6 小时
        adjusted_time = original_time + timedelta(hours=TIMEZONE_OFFSET)
        
        # 返回调整后的时间部分，格式为 HH:MM
        return adjusted_time.strftime("%H:%M")
    except Exception as e:
        print(f"处理时间时出错: {e}")
        return ""

# 从文件中读取 JSON
def read_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到")
        return None

# 将结果写入新的 JSON 文件
def write_json(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"数据成功写入 {file_path}")
    except Exception as e:
        print(f"写入文件时出错: {e}")

# 主函数
def main():
    # 读取原始 JSON 文件
    data = read_json(input_file)
    
    if data:
        # 提取所需数据
        extracted_data = extract_data(data)
        
        # 将提取的数据写入新的 JSON 文件
        write_json(extracted_data, output_file)

# 执行主函数
if __name__ == "__main__":
    main()
