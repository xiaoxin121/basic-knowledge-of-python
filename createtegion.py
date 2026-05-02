import json

# 假设你有一个 JSON 文件：china_regions.json
# 结构如：[{ "code": "110000", "name": "北京市", "children": [...] }]

with open('china_regions.json', encoding='utf-8') as f:
    data = json.load(f)

def gen_sql(items, parent_id=None, level=1):
    sqls = []
    for item in items:
        code = item['code']
        name = item['name']
        sql = f"INSERT INTO region (code, name, level, parent_id) VALUES ('{code}', '{name}', {level}, {parent_id if parent_id else 'NULL'});"
        sqls.append(sql)
        # 递归子级
        if 'children' in item:
            # 这里需要先插入父级，获取其 ID（实际需用程序查 ID 或用 code 关联）
            # 简化起见，假设用 code 关联，实际生产建议分步插入或用临时表
            pass
    return sqls