import pymysql
import os
import sys

class MySQL_Pet_DB:
    
    def __init__(self):
        username= "root"
        password = "MiNoviaRomualdaValeria$"
        mysql_db = "pet_adopt_system"
        mysql_host = "127.0.0.1"
        
        self.mysql_connection = pymysql.connect(host= mysql_host, user = username, password = password, database = mysql_db, cursorclass = pymysql.cursors.DictCursor, autocommit = True)
        
    def registrar_nueva_mascota(self, name, color, race, meassure1, attribute):
        
        try: 
            with self.mysql_connection.cursor() as cursor:
                query = "INSERT INTO pet (`name`,`color`,`race`)\
                    VALUES(%s,%s,%s)"
                cursor.execute(query, (name, color, race))
                proxid = cursor.lastrowid
                if race == 'dog':
                     query = "INSERT INTO dogs (`iddogs`,`ear_size`,`bark`)\
                         VALUES(%s,%s,%s)"
                     cursor.execute(query, (proxid, meassure1, attribute))
                elif race == 'cat':
                  query = "INSERT INTO cats (`idcats``human_hate`,`meow`)\
                      VALUES(%s,%s,%s)"
                  cursor.execute(query, (proxid, meassure1, attribute))
                elif race == 'bird':
                   query = "INSERT INTO birds (`idbirds``wing_size`,`fly_high`)\
                      VALUES(%s,%s,%s)"
                   cursor.execute(query, (proxid, meassure1, attribute))
                return("Pet created succesfully")
        except pymysql.ProgrammingError as e:
            print(f"Error al crear mascota {e}")
            sys.exit()