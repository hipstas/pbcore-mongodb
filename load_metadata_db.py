#!/usr/bin/python

from pymongo import MongoClient
import os
import unicodecsv
from bson import json_util
import xmltodict
import json

try: os.system('wget https://github.com/hipstas/pbcore-mongodb/blob/master/AAPB_Metadata_1.zip?raw=true -O AAPB_Metadata_1.zip')
except: pass

try: os.system('wget https://github.com/hipstas/pbcore-mongodb/blob/master/AAPB_Metadata_2.zip?raw=true -O AAPB_Metadata_2.zip')
except: pass

try: os.system('unzip AAPB_Metadata_1.zip')
except: pass

try: os.system('unzip AAPB_Metadata_2.zip')
except: pass

filenames_1 = ['AAPB_Metadata_1/'+item for item in os.listdir('AAPB_Metadata_1')if '.pbcore' in item.lower()]
filenames_2 = ['AAPB_Metadata_2/'+item for item in os.listdir('AAPB_Metadata_2') if '.pbcore' in item.lower()]

pbcore_paths = filenames_1 + filenames_2

#print len(pbcore_paths)


## Loading metadata into MongoDB
mongo_client=MongoClient('mongo', 27017)
db=mongo_client.pbcore_metadata


db.record.drop()


import timeit
tic=timeit.default_timer()

for xml_path in pbcore_paths:
    json_text=''
    json_data = xmltodict.parse(open(xml_path).read())
    json_text = json.dumps(json_data)
    data = json_util.loads(json_text)
    db.record.insert_one(data)

print("Completed loading database in "+str(timeit.default_timer() - tic)+" seconds")
