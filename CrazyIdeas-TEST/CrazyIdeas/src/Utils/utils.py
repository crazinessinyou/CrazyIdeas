import json

def parse_json(json_input):
    try:
        decoded_json = json.loads(json_input)  
        logger.info("Json parsed : " + decoded_json)
        return decoded_json
    except (ValueError, KeyError, TypeError):
        logger.error( "JSON format error")

def create_json(str):
    try:
        encoded_json = json.dumps(str)
        logger.info("Json encoded : " + encoded_json)
        return encoded_json
    except:
        logger.error( "Cannot convert into JSON")