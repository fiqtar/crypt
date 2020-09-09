import json

with open('sc_cfgs.json', 'r') as reader:
    cfg = reader.read()
    
def cr():
    data_link = json.loads(cfg)['link']
    # cdir /data/
    # mkdir /id_dcr/
    # put key, data
