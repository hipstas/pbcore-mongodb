#!/usr/bin/python

from pymongo import MongoClient
import os
import unicodecsv
from bson import json_util
import xmltodict
import json


os.chdir('/home/')

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


## Loading metadata into MongoDBs
mongo_client=MongoClient('mongo', 27017)
db=mongo_client.pbcore_metadata


import timeit
tic=timeit.default_timer()


def merge_dicts(list_of_dicts,item):
    result = {}
    if type(list_of_dicts)==dict:
        list_of_dicts = [list_of_dicts]
    if type(list_of_dicts)==None:
            return result
    try:
        if len(list_of_dicts)==0:
            return result
    except:
        print "&&&&&&&&&"
        print(list_of_dicts)
    for d in list_of_dicts:
        if type(d)==dict:
            keys = [item for item in d]
            for key in keys:
                if key[0]=="@":
                    try:
                        result.update({d[key].replace('.','<<dot>>'): d["#text"]})
                    except:
                        print("Guessing classes didn't work for "+str(d))
        elif (type(d)==str)|(type(d)==unicode):
            result.update({item: d})
        elif (type(d)==None):
            foo="great"
        else:
            print('*&^*')
            print(str(item)+'.'+str(d)+" is not a dict")
    return result


db.metadata.drop()

for xml_path in pbcore_paths: #### undo this
    json_text=''
    json_data = xmltodict.parse(open(xml_path).read())
    json_text = json.dumps(json_data['pbcoreDescriptionDocument'])
    data = json_util.loads(json_text)
    try:
        merged_dicts={}
        for item in data:
            if item!=None:
                if item[0]!='@':
                    #print('---')
                    #print(item)
                    list_of_dicts=data[item]
                    if list_of_dicts != None:
                        merged_dicts.update({item.replace('.','<<dot>>'):merge_dicts(list_of_dicts,item)})
        merged_dicts.update({"full_text_lower":str(json_text).lower()})
        temp = json.dumps(merged_dicts)
        temp = json_util.loads(temp)
        db.metadata.insert_one(temp)
    except Exception as e:
        print(e)

#print(db.metadata.find()[0])


print("Completed loading database in "+str(timeit.default_timer() - tic)+" seconds")


## Searching full text of each metadata

temp_items=[]

search_term='niversity'

search_term=search_term.lower()
for item in db.metadata.find({ 'pbcoreAnnotation.organization' : {'$regex':'.*'+search_term+'.*'}}):
    print(item)
    temp_items.append(item)

len(temp_items)




#temp_items=[]

#search_term='University'

#search_term=search_term.lower()
#for item in db.metadata.find({ "full_text_lower" : {'$regex':'.*'+search_term+'.*'}}):
#    print(item)
#    temp_items.append(item)

#len(temp_items)








#db.metadata.ensure_index(
#    [
#        ('pbcoreAnnotation.organization', 'text')
#    ],
#    name="search_index"
#)




#SEARCH_LIMIT=1000
#query=search_term
#text_results = db.command('text', metadata, search=query, limit=SEARCH_LIMIT)
