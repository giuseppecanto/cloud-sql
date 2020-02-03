import pymysql.cursors
import json

# Load database connection parameters
file_path = "conf/database.json"
with open(file_path) as db_conf_file:
    db_conf_params = json.load(db_conf_file)


# Connect to the database
connection = pymysql.connect(
    host = db_conf_params["HOST"],
    user = db_conf_params["DB_USER"],
    password = db_conf_params["DB_PASS"],
    db = db_conf_params["DB_NAME"],
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor)

# Get data
try:
    with connection.cursor() as cursor:
        sql_statement = "SELECT * FROM `<YOUR TABLE HERE>`"
        cursor.execute(sql_statement)
        results = cursor.fetchall()
        print(results)

    connection.commit()

except Exception as e:
    print("[ERROR] Found error:", e)

finally:
    connection.close()