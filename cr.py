import json

with open('cr_cfgs.json', 'r') as reader:
    cfg = reader.read()
    
def cr():
	data_link = json.loads(cfg)['link']
 	# cdir /data/
	# mkdir /id_cr/
	# put key, data
