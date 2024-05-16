import mysql.connector
import yaml

db = yaml.safe_load(open("secrets.yaml"))

# Establish a connection to the MySQL server
cnx = mysql.connector.connect(
    host=db["DB_HOST"],
    user=db["DB_USER"],  # both root and andrewcbuensalida works
    password=db["DB_PASSWORD"],
)

# Create a cursor object
cursor = cnx.cursor()

# Use the created database
cursor.execute("USE mrts")

# Execute the SQL query
cursor.execute("SELECT * FROM sales")

# Fetch all the rows from the result set
rows = cursor.fetchall()

# Print the rows
for row in rows:
  print(row)