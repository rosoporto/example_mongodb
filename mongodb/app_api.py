from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.errors import PyMongoError


app = Flask(__name__)


# Подключение к MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.mydatabase
collection = db.mycollection


@app.route('/items', methods=['GET'])
def get_items():
    try:
        items = list(collection.find({}, {'_id': 0}))
        return jsonify(items), 200
    except PyMongoError as e:
        return jsonify({'error': str(e)}), 500


@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Invalid input, name is required'}), 400

    try:
        collection.insert_one(data)
        return jsonify({'message': 'Item added successfully'}), 201
    except PyMongoError as e:
        return jsonify({'error': str(e)}), 500


@app.route('/items/<string:name>', methods=['GET'])
def get_item(name):
    try:
        item = collection.find_one({'name': name}, {'_id': 0})
        if item:
            return jsonify(item), 200
        return jsonify({'message': 'Item not found'}), 404
    except PyMongoError as e:
        return jsonify({'error': str(e)}), 500


@app.route('/items/<string:name>', methods=['PUT'])
def update_item(name):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        result = collection.update_one({'name': name}, {'$set': data})
        if result.matched_count > 0:
            return jsonify({'message': 'Item updated successfully'}), 200
        return jsonify({'message': 'Item not found'}), 404
    except PyMongoError as e:
        return jsonify({'error': str(e)}), 500


@app.route('/items/<string:name>', methods=['DELETE'])
def delete_item(name):
    try:
        result = collection.delete_one({'name': name})
        if result.deleted_count > 0:
            return jsonify({'message': 'Item deleted successfully'}), 200
        return jsonify({'message': 'Item not found'}), 404
    except PyMongoError as e:
        return jsonify({'error': str(e)}), 500


def clear_collection():
    collection.delete_many({})


if __name__ == '__main__':
    clear_collection()  # Очистка коллекции перед запуском приложения
    app.run(debug=True)
