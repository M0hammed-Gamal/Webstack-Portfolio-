from flask import Flask, request, jsonify

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/hello')
def hello():
    return "hello, how are you"


if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)

