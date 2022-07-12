# -*- coding: utf-8 -*-
"""
@author: Francisco Rodriguez Alfaro
@email: info@datamanagement.es
"""
import mysql.connector
from mysql.connector import errorcode

class Connection():
    
    USER = None
    PASS = None
    HOST = None
    DATABASE = None
    
    conn = None
    
    def __init__(self, USER, PASS, HOST, DATABASE ):
        
        self.USER = USER
        self.PASS = PASS
        self.HOST = HOST
        self.DATABASE = DATABASE
        
        try:
          cnx = cnx = mysql.connector.connect(user=self.USER
                                              , password=self.PASS
                                              , host=self.HOST
                                              , database=self.DATABASE)
          
          cnx.autocommit = False
          
          print("conectado a BBDD")
          self.conn = cnx
          
        except mysql.connector.Error as err:
            
          if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
          elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
          else:
            print(err)
        
    def execQuery(self, Query_params, params):
        cursor = self.conn.cursor()
        cursor.execute(Query_params, params)
    
    def execQueryArray( self, Query_params, paramsArray ):
        cursor = self.conn.cursor()
        cursor.executemany(Query_params, paramsArray)
    
    def commit(self):
        """ Para confirmar los inserts, se tiene que terminar con un commit """
        self.conn.commit()
        #print("commit")
    
    
    def execQuerySimple(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()


"""
con = Connection()
con.commit()




"""











