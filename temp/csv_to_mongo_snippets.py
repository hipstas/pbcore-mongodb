#Thank you for the suggestion.This one is the corrected code:


#wget https://github.com/stevemclaugh/pennsound-clone/blob/master/PennSound_metadata.csv?raw=true


import unicodecsv
from pymongo import MongoClient

csvfile = open('PennSound_metadata.csv', 'r')
reader = unicodecsv.DictReader( csvfile )
mongo_client=MongoClient('mongo', 27017)
db=mongo_client.pennsound

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
        print(counter)
        print(timeit.default_timer() - tic)
    except:
        print("ERROR: "+str(each))



####

#cursor = db.record.find({ 'author' :  {'$regex':'.*Bernstein.*'}})

#for item in cursor:
#    print item


from pymongo import MongoClient

mongo_client=MongoClient('mongo', 27017)

db=mongo_client.pennsound


def display_record(record_dict):
    print(
    record_dict['author']+' | '+ \
    record_dict['title']+' | '+ \
    record_dict['album']+' | '+ \
    record_dict['year']+' | '+ \
    '''<a href="'''+record_dict['url']+'''">link</a>'''
    )

def search_author(author_name):
    cursor = db.record.find({ 'author' :  {'$regex':'.*'+author_name+'.*'}})
    search_results=[]
    for item in cursor:
        search_results.append(display_record(item))
    return search_results

search_author('Filreis')
