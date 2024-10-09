#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:28:29 2024

@author: michaelevans1_snhu
"""
from pymongo import MongoClient
from pprint import pprint

class MongoCRUD(object) :
    
    def __init__(self, user: str, password : str):
        #This is the initialization method and will be where we initialize the MongoClient
        
        #Connection Variables
        
        USER = user
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31773
        DB = 'AAC'
        COL = 'animals'
        
        #Initialize Connection
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
    
    def create(self, **kwargs):
        
        try:
            #kwargs will be a dictionary containing key-value pairs that will act as the document
            
            document = kwargs
            
            #we will now insert the document into the collection and collect the result of the insert 
            #insert_result.acknowledged will be true if insert was successful and false if insert was unsuccessful
            #insert_one documetnation : https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.insert_one
            
            insert_result = self.collection.insert_one(document)
            
            #Finally we will check if the insert was successful
            
            if insert_result.acknowledged :
                return True
            else:
                return False
            
        except Exception as e:
            
            print(f"An error occurred during insertion: {e}")
            return False
        
        
    def read(self, document_filter={}):
        
        try : 
        
            #We will locate documents using the find method and a dictionary which will be constructed elsewhere in our code
            #filter is a dictionary that will accept a pre-made dictionary by the user. If the dictionary is not passed, it will
            #default to an empty dictionary which will trigger the method to return all documents. 
            
            document_search_results = self.collection.find(document_filter)
            
            #convert the results into a list
            documents = list(document_search_results)
            
            # If the document exists, return it; otherwise, return None
            if documents:
                return documents
            else:
                print("No documents found.")
                return [] #return an empty list
            
        except Exception as e:
            
            print(f"An error occurred during the read operation: {e}")
            return None
        
    def update(self, filter_criteria: dict, update_values: dict):
        try:
            #we will update documents using the update_one method
            update_result = self.collection.update_one(filter_criteria, {"$set": update_values})
            
            #If update_result exists, return the amount of documents updated. If it does not
            #Exist then print an error and return none. 
            if update_result:
                return update_result.modified_count
            else:
                print("Document not found, check inputs in method")
                return None
            
        except Exception as e:
           print(f"An error occurred during the read operation: {e}")
           return None
       
    def delete(self, **kwargs):
        try:
            document = kwargs
            
            delete_result = self.collection.delete_many(document)
            
            #if delete_result exists : print how many docs were deleted
            #else print a message that the attempt was unsuccessful
            if delete_result:
                return delete_result.deleted_count
            else:
                print("Document not found, check method inputs")
                return None
        
        except Exception as e:
            print(f"An error occurred during the read operation: {e}")
            return None
        
        
        
        
