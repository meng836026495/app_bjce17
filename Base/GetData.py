import yaml,os


# class GETDATA:

def get_yaml_data(file_name):
    arr = []
    with open('./data'+os.sep+file_name, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        for i in data.values():
            arr.append(tuple(i.values()))
            # return yaml.safe_load(f)
        return arr
