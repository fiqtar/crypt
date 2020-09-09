import json

with open('cr_cfgs.json', 'r') as reader:
    cfg = reader.read()
    
def dcr():
    data_link = json.loads(cfg)['link']
    # cdir /data/
    # mkdir /id_dcr/
    # put key, data
