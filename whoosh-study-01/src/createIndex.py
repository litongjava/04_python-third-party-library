import os
from whoosh.index import create_in
from whoosh.fields import *

# 定义Whoosh索引的字段
schema = Schema(path=TEXT(stored=True), content=TEXT)

# 创建Whoosh索引文件夹
index_dir = r"D:\index"
if not os.path.exists(index_dir):
    os.mkdir(index_dir)

# 创建Whoosh索引对象
ix = create_in(index_dir, schema)

# 获取目标目录下的所有文件路径
dir_path = r"E:\code\aliyun-function-calculation\demo"
file_paths = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

# 遍历所有文件并将它们添加到索引中
writer = ix.writer()
for path in file_paths:
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
        print(path)
        writer.add_document(path=path, content=content)
writer.commit()
