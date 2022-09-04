import psycopg2
from  psycopg2.extensions import ISOLATION_LEVEL_DEFAULT

##Connection Details for Postgres
host = '127.0.0.1'
user ='postgres'
password = 'postgres'
dbname = 'postgres'


#Connect to Master Database and Create Another Database"
con_string="host={0} dbname={1} user={2} password={3}".format(host,dbname,user,password)
conn = psycopg2.connect(con_string)
conn.set_session(autocommit=True)
#conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
print("Connection established")
cur=conn.cursor()

cur.execute("drop database if exists dwh_postgres")
cur.execute("create database dwh_postgres")
conn.close()

# Reconnect new Database which is created in Previous Step
dbname='dwh_postgres'
con_string="host={0} dbname={1} user={2} password={3}".format(host,dbname,user,password)
conn = psycopg2.connect(con_string)
print("Connection established")
cur = conn.cursor()

#Create Function to call Drop and Recreate tables
def drop_recreate(cur,tablename,create):
    cur.execute("drop table if exists {0}".format(tablename))
    cur.execute(create)
    print("Finished creating table {0}".format(tablename))

def populate_table(cur,file,tablename):
    f = open(file,"r")
    try:
        cur.copy_from(f,tablename,sep=",",null="")
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
        cur.close()
        print("Finished populating {0}".format(tablename))

if __name__== "__main__":


## Create Rider Table 
    table = "rider"
    filename = './data/riders.csv'
    create = "CREATE TABLE rider (rider_id INTEGER PRIMARY KEY, first VARCHAR(50), last VARCHAR(50), address VARCHAR(100), birthday DATE, account_start_date DATE, account_end_date DATE, is_member BOOLEAN);"

    drop_recreate(cur,table,create)
    populate_table(cur,filename,table)
    # Create Payment table
    table = "payment"
    filename = './data/payments.csv'
    create = "CREATE TABLE payment (payment_id INTEGER PRIMARY KEY, date DATE, amount MONEY, rider_id INTEGER);"

    drop_recreate(cur, table, create)
    populate_table(cur, filename, table)

    # Create Station table
    table = "station"
    filename = './data/stations.csv'
    create = "CREATE TABLE station (station_id VARCHAR(50) PRIMARY KEY, name VARCHAR(75), latitude FLOAT, longitude FLOAT);"

    drop_recreate(cur, table, create)
    populate_table(cur, filename, table)

    # Create Trip table
    table = "trip"
    filename = './data/trips.csv'
    create = "CREATE TABLE trip (trip_id VARCHAR(50) PRIMARY KEY, rideable_type VARCHAR(75), start_at TIMESTAMP, ended_at TIMESTAMP, start_station_id VARCHAR(50), end_station_id VARCHAR(50), rider_id INTEGER);"

    drop_recreate(cur, table, create)
    populate_table(cur, filename, table)

    # Clean up
    cur.close()
    conn.close()

    print("All done!")

     


        

