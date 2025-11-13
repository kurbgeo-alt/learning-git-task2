


from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db',echo = True)

meta = MetaData()

stations = Table(
   'stations', meta,
   Column('id', Integer, primary_key=True),
   Column('station', String),
   Column('latitude', Integer),
   Column('longitude',Integer),
   Column('elevation', Integer),
   Column('name', String),
   Column('country', String),
   Column('state',String),
   # <- DODAJ TO
)
stations2 =Table(
    'stations2',meta,
    Column('id', Integer, primary_key = True),
    Column('station', String),
    Column('date', String),
    Column('precip',Integer),
    Column('tobs',Integer),

    
)


meta.create_all(engine)
print(engine.table_names())



ins = stations.insert()

ins = stations.insert().values(station='USC00519397',latitude ='21.2716', longitude = '-157.8168', elevation = 3.0, name = 'WAIKIKI 717.2', country = 'US', state = 'HI')

conn = engine.connect()
result = conn.execute(ins)
conn.execute(ins,[
    {'station': 'USC00513117', 'latitude': '21.4234', 'longitude': '-157.8015', 'elevation': 14.6, 'name':  'KANEOHE 838.1', 'country': 'US', 'state': 'HI'},
    {'station': 'USC00514830', 'latitude': '21.5213', 'longitude': '-157.8374', 'elevation': 7.0, 'name': 'KUOLA 874.3, ', 'country' : 'US', 'state': 'HI'},
    {'station':'USC00517948' , 'latitude': '21.3934', 'longitude': '-157.9751', 'elevation': 11.9, 'name': 'PEARL CITY ', 'country': 'US', 'state': 'HI'},
    {'station': 'USC00518838', 'latitude': '21.4992', 'longitude': '-157.9432', 'elevation': 306.6, 'name': 'UPPER WAHIAMA 874.6', 'country': 'US', 'state': 'HI'},
    {'station': 'USC00519523', 'latitude': '21.3356', 'longitude': '-157.7114', 'elevation': 19.5, 'name': 'WAIMANALO EXPERIMENTAL FARM', 'country': 'US', 'state': 'HI'},
    {'station': 'USC00519281', 'latitude': '21.4517', 'longitude': '-157.8489', 'elevation': 32.0, 'name': 'WAIHEE 837.5', 'country': 'US', 'state': 'HI'},
    {'station': 'USC00511918', 'latitude': '21.4712', 'longitude': '-157.8025', 'elevation': 3.4,  'name': 'HONOLULU OBSERVATORY 702.2','country': 'US', 'state': 'HI'},
    {'station': 'USC00516128', 'latitude': '21.3331', 'longitude': '-157.8915', 'elevation': 152.4, 'name': 'MANOA LYON ARBO 785.2', 'country': 'US', 'state': 'HI'},
])

ins = stations2.insert().values(station='USC0051937', date='2010--01-01',precip=0.0,tobs=65)
conn = engine.connect()
result = conn.execute(ins)
conn.execute(ins,[
    {'station':'USC00519397', 'date':'2010-01-02', 'precip':0.0, 'tobs':63},
    {'station': 'USC00519397', 'date':'2010-01-03', 'precip':0.0,'tobs':74},
    {'station': 'USC00519397', 'date': '2010-01-04', 'precip':0.0,'tobs':76},
    {'station': 'USC00519397', 'date': '2010-01-06','precip':0.0,'tobs':73},
    {'station':'USC00519397','date':'2010-01-07','precip':0.06,'tobs':70},
    {'station': 'USC00519397', 'date': '2010-01-08', 'precip':0.0,'tobs':64},
    {'station': 'USC00519397', 'date': '2010-01-09', 'precip':0.0, 'tobs': 68},
    {'station':'USC00519397', 'date': '2010-01-10', 'precip':0.0,'tobs':73},
    {'station':'USC00519397', 'date':'2010-01-11', 'precip':0.01,'tobs':64},
    {'station':'USC00519397', 'date':'2020-01-12','precip':0.0, 'tobs':61},
    {'station':'USC00519397', 'date': '2010-01-14','precip':0.0,'tobs':66},
    {'station':'USC00519397', 'date': '2010-01-15','precip':0.0,'tobs':65},
    {'station': 'USC00519397','date':'2010-01-16','precip':0.0,'tobs':68},
    {'station': 'USC00519397', 'date': '2010-01-17','precip':0.0,'tobs':64},
    {'station': 'USC00519397', 'date': '2010-01-18','precip':0.0,'tobs': 72},
    {'station': 'USC00519397', 'date': '2010-01-19','precip':0.0,'tobs':66},
    {'station': 'USC00519397', 'date': '2010-01-20','precip':0.0,'tobs':66},
    {'station':'USC00519397', 'date': '2010-01-21','precip':0.0,'tobs':69},
    {'station':'USC00519397', 'date':'2010-01-22','precip':0.0,'tobs':67},
    {'station':'USC00519397', 'date':'2020-01-23','precip':0.0,'tobs':67},
    {'station':'USC00519397', 'date': '2010-01-24','precip':0.01,'tobs':71},
    {'station':'USC00519397', 'date': '2010-01-25','precip':0.0,'tobs':67},
    {'station':'USC00519397','date':'2010-01-26','precip':0.04, 'tobs':76},
    {'station':'USC00519397','date':'2010-01-27','precip':0.12,'tobs':68},
    {'station':'USC00519397','date':'2010-01-28', 'precip':0.0,'tobs':72},
    {'station':'USC00519397','date':'2010-01-30','precip':0.0,'tobs':70},
    {'station':'USC00519397','date':'2010-01-31','precip':0.03,'tobs':67},
    
])
conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
conn = engine.connect()
s = stations.select().where (stations.c.state == 'HI')
result = conn.execute(s)
for row in result:
    print(row)
  


    
    
    

   
