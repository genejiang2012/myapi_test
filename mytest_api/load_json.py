import json

json_file_path = r"D:/brand_channel.json"

with open(json_file_path, 'r', encoding='utf-8') as json_file:
    json_2_dict = json.load(json_file)
    brand_list = json_2_dict['data'][0]['value']
    
    department_dict = {}

    print(brand_list)

    for _, item in enumerate(brand_list):
        print(item['name'], item['parentId'])
        if item['parentId'] == 69:
            department_dict.setdefault('dep_name', []).append(item['name'])
            department_dict.setdefault('dep_id', []).append(item['id'])
        elif item['parentId'] in department_dict['dep_id']:
            department_dict.setdefault('center_name', []).append(item['name'])
            department_dict.setdefault('center_id', []).append(item['id'])
        elif item['parentId'] in department_dict['center_id']:
            department_dict.setdefault('group_name', []).append(item['name'])
            department_dict.setdefault('group_id', []).append(item['id'])
        elif item['parentId'] in department_dict['group_id']:
            department_dict.setdefault('brand_name', []).append(item['name'])
            department_dict.setdefault('brand_id', []).append(item['id'])
 

    print(department_dict)
