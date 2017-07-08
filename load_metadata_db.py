#!/usr/bin/python

from pymongo import MongoClient
import os
import unicodecsv

os.chdir('/home/')

## Loading metadata into MongoDB
mongo_client=MongoClient('mongo', 27017)
db=mongo_client.pennsound

csvfile = open('/home/PennSound_metadata.csv', 'r')
reader = unicodecsv.DictReader( csvfile )

db.record.drop()
header= [ 'url','author','title','album','genre','year','comments','track_no','composer','content_group','band','conductor','interpreted_by','location','encoded_by','album_artist','album_type','audio_source_url','commercial_url','copyright_url','encoding_date','internet_radio_url','play_count','publisher','publisher_url','original_release_date','recording_date','release_date','tagging_date','terms_of_use','id3_version','processing_error']

counter=0

for each in reader:
    try:
        row={}
        for field in header:
            row[field]=each[field]
        db.record.insert(row)
        counter+=1
        #print(counter)
    except:
        print("ERROR: "+str(each))
