# import os
# import shutil
# import re
#
# # 定义源文件夹和目标文件夹
# source_dir = '/home/yanghan/CFLD/fashion/train_highres/fashion'
# target_dir = '/home/yanghan/CFLD/fashion/train_highres/'
#
# # 遍历源文件夹中的所有文件
# for root, dirs, files in os.walk(source_dir):
#     for file in files:
#         # 获取原文件路径
#         original_file_path = os.path.join(root, file)
#
#         # 提取类别、item_id 和 image_num，并重命名文件
#         match = re.match(r'.*/fashion/([^/]+)/([^/]+)/id_(\d{8})/(\d+)_(\w+)\.jpg$', original_file_path.replace('\\', '/'))
#         if match:
#             category = match.group(1).replace('/', '')
#             sub_category = match.group(2).replace('/', '')
#             item_id = match.group(3)
#             image_num = match.group(4)  # 获取数字部分
#             image_desc = match.group(5)  # 获取图像描述部分（如 front, back 等）
#
#             # 按指定格式重命名，保留 image_num 和 image_desc 的下划线
#             new_file_name = f"fashion{category}{sub_category}id{item_id}{image_num}_{image_desc}.jpg"
#             new_file_name = new_file_name.rsplit('_', 1)  # 按最后一个 _ 分割
#             new_file_name = ''.join(new_file_name)  # 合并为新的文件名
#
#
#             # 构建目标文件路径
#             new_file_path = os.path.join(target_dir, new_file_name)
#
#
#
#             # 复制并重命名文件到目标目录
#             shutil.copy2(original_file_path, new_file_path)
#             print(f"Copied and renamed: {original_file_path} -> {new_file_path}")

import os
import shutil
import re

# 定义源文件夹和目标文件夹
source_dir = '/home/yanghan/CFLD/fashion/train_highres/fashion'
target_dir = '/home/yanghan/CFLD/fashion/train_highres/'

# 用于跟踪已处理的文件
processed_files = set()

# 遍历源文件夹中的所有文件
for root, dirs, files in os.walk(source_dir):
    for file in files:
        # 获取原文件路径
        original_file_path = os.path.join(root, file)

        # 确保文件没有被重复处理
        if original_file_path in processed_files:
            continue

        # 提取类别、item_id 和 image_num，并重命名文件
        match = re.match(r'.*/fashion/([^/]+)/([^/]+)/id_(\d{8})/(\d+)_(\w+)\.jpg$',
                         original_file_path.replace('\\', '/'))
        if match:
            category = match.group(1).replace('/', '')
            sub_category = match.group(2).replace('/', '')
            item_id = match.group(3)
            image_num = match.group(4)  # 获取数字部分
            image_desc = match.group(5)  # 获取图像描述部分（如 front, back 等）

            # 按指定格式重命名，保留 image_num 和 image_desc 的下划线
            new_file_name = f"fashion{category}{sub_category}id{item_id}{image_num}_{image_desc}.jpg"
            new_file_name = new_file_name.rsplit('_', 1)  # 按最后一个 _ 分割
            new_file_name = ''.join(new_file_name)  # 合并为新的文件名

            # 构建目标文件路径
            new_file_path = os.path.join(target_dir, new_file_name)

            # 复制并重命名文件到目标目录
            shutil.copy2(original_file_path, new_file_path)
            print(f"Copied and renamed: {original_file_path} -> {new_file_path}")

            # 将已处理的文件路径添加到集合中
            processed_files.add(original_file_path)





