from pymongo import MongoClient
import logging

class db_connection_utils():
       client = MongoClient()
       db_connection = None
       logger = logging.getLogger(__name__)
       
       def connect_to_database(self):
           if self.db_connection != None:
               self.close_connection()
           try:
               self.client = MongoClient(self.host, self.port)
               self.logger.info("Database Connection established")
               self.db_connection = self.select_database() 
               return self.db_connection   
           except:
                self.logger.error("Database Connection failed")
                raise ValueError("could not connect to the database :: HostName:" + self.host +" PortNumber:" + self.port)  
           
       def select_database(self):
           try:
               db = client[self.db_name]
               self.logger.info(self.db + " Database Selected")
               return db
           except:
                self.logger.error(self.db + " Database not Selected")
                raise ValueError("could not connect to the database :: DBName:" + self.db_name)
       
       def close_connection(self):
           self.client.close()
           self.logger.info("Database Connection closed")
       
       def select_collection(self, collection_name):
           try:
               collection = self.db_connection[collection_name]
               self.logger.info("Collection Selected :: CollectionName : " + collection)
               return collection
           except:
               self.logger.error("Collection not Selected :: CollectionName : " + collection)
               raise ValueError("could not connect to the collection :: CollectionName:" + collection)
                 
       def get_db_name(self):
            return self.db_name
        
       def set_db_name(self, database_name):
            self.db_name = database_name
    
       def __init__(self, host, port, database_name):
           self.host = host
           self.port = port
           self.db_name = database_name


