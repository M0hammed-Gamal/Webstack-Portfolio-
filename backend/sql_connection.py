import mysql.connector

cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='gs')
 
if cnx is None:
      print("Opening not mysql connection")

cursor = cnx.cursor()

query = "SELECT * FROM gs.product"

cursor.execute(query)

for (product_id, name, uom_id, price_per_unit) in cursor:
    print(product_id, name, uom_id, price_per_unit)

cnx.close()