import psycopg2
import traceback
from psycopg2 import sql
from datetime import datetime, timedelta
from .config import Settings

def dbConnect():

    try:

        settings = Settings()

        conn = psycopg2.connect(
            dbname = settings.dbName,
            user = settings.dbUsername,
            password = settings.dbPassword,
            host = settings.dbHostname,
            port = settings.dbPort
        )

        print("Database connection successful!")
        return conn
    
    except psycopg2.OperationalError as e:
        print(f"Operational error occurred: {e}")
        print("Traceback details:", traceback.format_exc())
        return None
    except psycopg2.InterfaceError as e:
        print(f"Interface error occurred: {e}")
        print("Traceback details:", traceback.format_exc())
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Traceback details:", traceback.format_exc())
        return None






def update_date():
    current_date = datetime.now().date()
    print(current_date)

    conn = dbConnect()

    if conn is None:
        print("someting went wrong")
        return
    
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM daily_record ORDER BY day_id DESC LIMIT 1")

    id = cursor.fetchone()

    did = id[0] 
    date = id[1]
    
    print(did)
    print(date)

    if date == current_date:

        print("welcome back!")

    else:

        difference = current_date - date
        dp = difference.days

        for x in range(1, dp+1):

            nid = did + x
            ndate = date + timedelta(days=x)
            cursor.execute(f"INSERT INTO daily_record (day_id, date, score) VALUES (%s, %s, %s)", (nid, ndate, 0))

        conn.commit() 

    cursor.close()
    conn.close()

def get_dates():

    conn = dbConnect()

    cursor = conn.cursor()

    cursor.execute(f"SELECT date FROM daily_record ORDER BY day_id DESC LIMIT 7")

    dates = cursor.fetchall()

    day = []

    for date in (dates):
        days = date[0].strftime("%Y-%m-%d")
        day.append(days)

    #day.pop(0)  
    return day

    