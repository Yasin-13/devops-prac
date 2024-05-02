from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask!"

@app.route('/api/data')
def get_data():
    data = {'name': 'Yasin', 'age': 20, 'city': 'Mumbai'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
