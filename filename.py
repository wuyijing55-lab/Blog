import os
import re
from datetime import datetime

# _posts 目录
posts_dir = "_posts"

# 日期正则
pattern = re.compile(r"^\d{4}-\d{2}-\d{2}-.+\.md$")

# 遍历目录
for filename in os.listdir(posts_dir):
    if not filename.endswith(".md"):
        continue
    if pattern.match(filename):
        # 已经是标准格式，跳过
        continue

    old_path = os.path.join(posts_dir, filename)
    # 使用文件修改日期作为日期
    timestamp = os.path.getmtime(old_path)
    date_str = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
    
    # 生成新的文件名：YYYY-MM-DD-原名.md
    safe_name = filename.replace(" ", "_").replace(".", "_")
    new_filename = f"{date_str}-{safe_name}"
    new_path = os.path.join(posts_dir, new_filename)

    # 避免覆盖已有文件
    counter = 1
    while os.path.exists(new_path):
        new_filename = f"{date_str}-{counter}-{safe_name}"
        new_path = os.path.join(posts_dir, new_filename)
        counter += 1

    os.rename(old_path, new_path)
    print(f"Renamed: {filename} -> {new_filename}")

print("✅ 完成所有文件重命名")
