import yaml

# with open('./value2.yml','r',encoding='utf-8') as f:
#     data = yaml.safe_load(f)
#     print(data)
#     print(type(data.get('people')))



with open('./ww.yml','a') as f:
    yaml.dump(data,f)