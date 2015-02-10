import pymongo
from Utils import utils
from Utils import db_connection_utils

class create_idea():
    
    def __init__(self):
        self.db = new db_connection_utils(,,CrazyIdeas)
        
def create_idea(idea_json):
    decoded_json = utils.parse_json(idea_json)
    result = validate_json(decoded_json)
    if result == 1:
        
    make insert query in Ideas
    get idea id
    find user with user if not create a new tag 
    check tag id exists in tag if 
    update idea for user id
    
    
    
    ## tags, user, idea