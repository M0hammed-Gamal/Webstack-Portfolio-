from flask import Flask, request, jsonify
import products_dao
from sql_connection import get_sql_connection

app = Flask(__name__)


connection = get_sql_connection()

@app.route('/getproduct' , methods=['GET'])
def get_product():
    product = products_dao.get_all_products(connection)
    response = jsonify(product)
    response.headers.add('Access-control-Allow-origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)