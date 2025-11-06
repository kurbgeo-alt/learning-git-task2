import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)

   return conn

def execute_sql(conn, sql):
   """ Execute sql
   :param conn:
   Connection object
   :param sql: a SQL script
   :param sql: a SQL script
   :return:
   """
   print("SQL:", sql)

   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

def add_(conn, travel):
   """
   Create a new into the travel table
   :param conn:
   :param place:
   :return: travel id
   """
   sql = '''INSERT INTO travels(nazwa_kraju, data_wyjazdu, data_przyjazdu)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, travel)
   return cur.lastrowid
def add_travel(conn, travel):
   """
   Create a new travel into the travels table
   :param conn:
   :param travel:
   :return: travel id
   """
   sql = '''INSERT INTO travels(nazwa_kraju, data_wyjazdu, data_przyjazdu) 
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, travel)
   conn.commit()
   return cur.lastrowid

def add_place(conn, place):
   """
   Create a new place into the places table
   :param conn:
   :param place:
   :return: place id
   """
   sql = '''INSERT INTO places(travel_id, miejsce_id, nazwa_kraju, opis, status, data_wyjazdu, data_przyjazdu)
             VALUES(?,?,?,?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, place)
   conn.commit()
   return cur.lastrowid

def select_place_by_status(conn, status):
   """
   Query places by priority
   :param conn: the Connection object
   :param status:
   :return:
   """
   cur = conn.cursor()
   cur.execute("SELECT * FROM places WHERE status=?", (status,))

   rows = cur.fetchall()
   return rows 

def select_all(conn, table):
   """
   Query all rows in the table
   :param conn: the Connection object
   :return:
   """
   cur = conn.cursor()
   cur.execute(f"SELECT * FROM {table}")
   rows = cur.fetchall()

   return rows

def select_where(conn, table, **query):
   """
   Query tasks from table with data from **query dict
   :param conn: the Connection object
   :param table: table name
   :param query: dict of attributes and values
   :return:
   """
   cur = conn.cursor()
   qs = []
   values = ()
   for k, v in query.items():
       qs.append(f"{k}=?")
       values += (v,)
   q = " AND ".join(qs)
   cur.execute(f"SELECT * FROM {table} WHERE {q}", values)

   rows = cur.fetchall()
   return rows

def update(conn, table, id, **kwargs):
   """
   update status, data_wyjazdu, and data_przyjazdu of a place
   :param conn:
   :param table: table name
   :param id: row id
   :return:
   """
   parameters = [f"{k} = ?" for k in kwargs]
   parameters = ", ".join(parameters)
   values = tuple(v for v in kwargs.values())
   values += (id, )

   sql = f''' UPDATE {table}
             SET {parameters}
             WHERE id = ?'''
   try:
       cur = conn.cursor()
       cur.execute(sql, values)
       conn.commit()
       print("OK")
   except sqlite3.OperationalError as e:
       print(e)

def delete_where(conn, table, **kwargs):
   """
   Delete from table where attributes from
   :param conn:  Connection to the SQLite database
   :param table: table name
   :param kwargs: dict of attributes and values
   :return:
   """
   qs = []
   values = tuple()
   for k, v in kwargs.items():
       qs.append(f"{k}=?")
       values += (v,)
   q = " AND ".join(qs)

   sql = f'DELETE FROM {table} WHERE {q}'
   cur = conn.cursor()
   cur.execute(sql, values)
   conn.commit()
   print("Deleted") 

def delete_all(conn, table):
   """
   Delete all rows from table
   :param conn: Connection to the SQLite database
   :param table: table name
   :return:
   """
   sql = f'DELETE FROM {table}'
   cur = conn.cursor()
   cur.execute(sql)
   conn.commit()
   print("Deleted")


   
         



   create_travels_sql = """
   -- travel table
   CREATE TABLE IF NOT EXISTS travels (
      id integer PRIMARY KEY,
      nazwa_kraju TEXT NOT NULL,
      data_wyjazdu TEXT,
      data_przyjazdu TEXT
   );
   """

   create_places_sql = """
   --   places table
   CREATE TABLE IF NOT EXISTS places (
      id integer PRIMARY KEY,
      travel_id integer NOT NULL,
      miejsce_id integer NOT NULL,
      nazwa_kraju VARCHAR(250) NOT NULL,
      opis TEXT,
      status VARCHAR(15) NOT NULL,
      data_wyjazdu text NOT NULL,
      data_przyjazdu text NOT NULL,
      FOREIGN KEY (travel_id) REFERENCES travels (id)
   );
   """
   if __name__ == "__main__":
     #delete_travels = """DROP TABLE IF EXISTS travels;"""
     #delete_places = """DROP TABLE IF EXISTS places;"""
     db_file ="database.db"


   

   conn = create_connection(db_file)
   if conn is not None:
       execute_sql(conn, create_travels_sql)
       execute_sql(conn, create_places_sql)
       conn.close()

 





   travel = ("Wycieczka do Londynu", "2020-05-11 00:00:00", "2020-05-13 00:00:00")

   conn = create_connection("database.db")
   travel_id = add_travel(conn, travel)

   place = (
       travel_id,
       "Londyn",
       1,
       "Interesujące miejsca w Londynie",
       "zamieszkany",
       "2020-05-11 12:00:00",
       "2020-05-11 15:00:00"
   )

   place_id = add_place(conn, place)

   print(travel_id, place_id)
   conn.commit()


conn = create_connection("database.db")
select_all(conn, "travels")
select_where(conn, "places", travel_id=1)

conn = create_connection("database.db")
update(conn, "places", 2, status="zamieszkany")
update(conn, "places", 2, status="zamieszkany")
conn.close()

conn = create_connection("database.db")
delete_where(conn,"places",id=3)
delete_all(conn,"places")





   




