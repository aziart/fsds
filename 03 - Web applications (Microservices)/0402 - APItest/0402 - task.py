# LOGGING LIBRARIES
import logging
logging.basicConfig(filename='03 - Web applications (Microservices)/0402 - APItest/0402 - task.log',
                    filemode='w',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
logging.info("Running Urban Planning")
logger = logging.getLogger('urbanGUI')
# MYSQL LIBRARY and CONNECTION
import mysql.connector as conn
from mysql.connector import Error
# PANDAS LIBRARY
import pandas as pd



car_data = pd.read_csv('03 - Web applications (Microservices)/data/car.data', index_col=False, delimiter = ',')
logging.info("CAR DATA SAMPLE: \n{}".format(car_data.head()))

try:
    logging.info("STEP 0: ESTABLISHING CONNECTION")
    mydb = conn.connect(host='localhost', user='root', password='12345678')
    if mydb.is_connected():


        cursor = mydb.cursor(buffered=True)

        logging.info("STEP 1: AVAILABLE DATABASES")
        cursor.execute('show databases')
        logging.info("AVAILABLE DATABASES ARE: \n{}".format(cursor.fetchall()))

        logging.info("STEP 2: CREATING CARDATASET DATABASE")
        cursor.execute('DROP DATABASE IF EXISTS CARDATASET;')
        cursor.execute('CREATE DATABASE CARDATASET')
        cursor.execute('show databases')
        logging.info("AVAILABLE DATABASES ARE: \n{}".format(cursor.fetchall()))

        logging.info('STEP 3: SELECTING DATABASE')
        cursor.execute('use CARDATASET')


        cursor.execute("select database();")
        record = cursor.fetchone()
        logging.info("You're connected to database: {}".format(record))
        
        
        cursor.execute('DROP TABLE IF EXISTS CAR;')
        logging.info('STEP 4: Creating table....')
        
        # in the below line please pass the create table statement which you want 
        # #to create
        cursor.execute("create table CAR(buying VARCHAR(6), \
                        maint VARCHAR(6), doors VARCHAR(6), persons VARCHAR(4),\
                        lug_boot VARCHAR(5), safety VARCHAR(4), class VARCHAR(6))")
        logging.info("Table is created....")
        #loop through the data frame
        for i,row in car_data.iterrows():
            #here %S means string values 
            sql = "INSERT INTO CARDATASET.CAR VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            # logging.info("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            mydb.commit()
        
        cursor.execute('select * from cardataset.car')
        logging.info('INSERTED DATASET SAMPLE')
        for i in cursor.fetchmany(10):
            logging.info(i)
        logging.info('STEP 5: CLOSING CONNECTION')
        mydb.close()
except Error as e:
            logging.info("Error while connecting to MySQL", e)

logging.info('DATA SUCCESSULLY INSERTED')
