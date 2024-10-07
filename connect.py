import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="user_db"
)

data = call_data
for x in data:
  print (x)


def call_data():
  cursor = db.cursor()
  query = "SELECT * FROM user_table"
  cursor.execute(query)
  data = cursor.fetchall()

#for x in data:
  #print(x)
#if db.is_connected():
  #print("Berhasil terhubung ke database")