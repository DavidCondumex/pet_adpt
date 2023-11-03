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
                  query = "INSERT INTO cats (`idcats`,`human_hate`,`meow`)\
                      VALUES(%s,%s,%s)"
                  cursor.execute(query, (proxid, meassure1, attribute))
                elif race == 'bird':
                   query = "INSERT INTO birds (`idbirds`,`wing_size`,`fly_high`)\
                      VALUES(%s,%s,%s)"
                   cursor.execute(query, (proxid, meassure1, attribute))
                return("Pet created succesfully")
        except pymysql.ProgrammingError as e:
            print(f"Error al crear mascota {e}")
            sys.exit()
             
    def traer_mascota(self, name):
        try:
            attribute_first = {}
            with self.mysql_connection.cursor() as cursor:
                query = f"SELECT * FROM pet WHERE name = '{name}'"
                cursor.execute(query)
                attribute_first = cursor.fetchall()[0]
                if attribute_first['race'] == 'dog':
                     query = f"SELECT ear_size, bark FROM dogs WHERE iddogs = {attribute_first['idpet']}"
                     cursor.execute(query)
                     attributes_2nd = cursor.fetchall()[0]
                elif attribute_first['race'] == 'cat':
                  query = f"SELECT human_hate, meow FROM cats WHERE idcats = {attribute_first['idpet']}"
                  cursor.execute(query)
                  attributes_2nd = cursor.fetchall()[0]
                elif attribute_first['race'] == 'bird':
                   query = f"SELECT wing_size, fly_high FROM birds WHERE idbirds = {attribute_first['idpet']}"
                   cursor.execute(query)
                   attributes_2nd = cursor.fetchall()[0]
            attribute_first.update(attributes_2nd)
            return attribute_first
                
        except pymysql.ProgrammingError as e:
            print(f"Error al ejcutar la consulta {e}")
            sys.exit()
            
    def lista_masoctas(self, lista):
        try:
            with self.mysql_connection.cursor() as cursor:
                query = f"SELECT * FROM {lista}"
                cursor.execute(query)
                consulta = cursor.fetchall()
                return consulta
        except pymysql.ProgrammingError as e:
            print(f"Error al ejcutar la consulta {e}")
            sys.exit()
            
    def adoptar_mascota(self, name):
        try:
            with self.mysql_connection.cursor() as cursor:
                query = f"DELETE FROM pet WHERE name = '{name}'"
                cursor.execute(query)
        except pymysql.ProgrammingError as e:
            print(f"Error al mover mascota del sistema {e}")
            sys.exit()