import pymongo
from Utils import utils

def get_thumbnail_values(idea_ID):
    idea_json = posts.find_one({"_id": idea_ID})
    decoded_idea_json = utils.parse_json(idea_json)
    
    thumbnail_json_str = {'date :'+ decoded_idea_json[date] + 'tried_id :' + decoded_idea_json[tried_id] + 'challenge :' + decoded_idea_json[challenge] +'likes:' + decoded_idea_json[likes] + 'comments :'+ decoded_idea_json[comments] + ' thumbnail :' + decoded_idea_json[thumbnail]}
    
    encoded_thumbnail_json= utils.create_json(thumbnail_json_str)
    return encoded_thumbnail_json