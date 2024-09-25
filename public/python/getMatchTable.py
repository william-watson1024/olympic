import requests
import json
from datetime import datetime, timedelta
import os

print("开始爬取数据...")
# 设置开始日期和结束日期
start_date = datetime(2024, 7, 24)
end_date = datetime(2024, 8, 11)

# 构建日期范围
date_range = (end_date - start_date).days + 1

# 基础 URL
base_url = "https://sph-s-api.olympics.com/summer/schedules/api/CHI/schedule/day/"

# 保存所有爬取的数据
all_data = []

# 循环抓取每天的数据
for day_offset in range(date_range):
    current_date = start_date + timedelta(days=day_offset)
    formatted_date = current_date.strftime("%Y-%m-%d")
    
    # 构造请求的 URL
    url = base_url + formatted_date
    
    try:
        # 发起请求
        response = requests.get(url)
        response.raise_for_status()  # 如果返回状态码不是200，会抛出异常
        
        # 获取JSON数据
        data = response.json()
        
        # 将数据添加到总列表
        all_data.append({
            "date": formatted_date,
            "data": data
        })
        print(f"成功爬取 {formatted_date} 的数据")
    
    except requests.exceptions.RequestException as e:
        print(f"请求 {url} 失败: {e}")

# 将数据保存为 JSON 文件
with open("olympic_schedule_2024.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=4)

print("数据爬取完成，已保存为 olympic_schedule_2024.json 文件")
