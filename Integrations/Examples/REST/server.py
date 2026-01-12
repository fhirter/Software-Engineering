from flask import Flask, jsonify, request, Response
from items_repository import ItemsRepository

app = Flask(__name__)

items_repository = ItemsRepository()

basePath = '/api/items'

@app.route(basePath, methods=['GET'])
def get_items():
    items = items_repository.get_all()
    return jsonify(items), 200


@app.route(basePath+'/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = items_repository.get(item_id)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404


@app.route(basePath, methods=['POST'])
def create_item():
    data = request.get_json()

    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    new_item = items_repository.create(
        name=data["name"],
        description=data.get("description", "")
    )

    response = Response(status=201)
    response.headers['Location'] = f"{basePath}/{new_item['id']}"

    return response


@app.route(basePath+'/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()

    updated_item = items_repository.update(
        item_id=item_id,
        name=data.get("name"),
        description=data.get("description")
    )

    if not updated_item:
        return jsonify({"error": "Item not found"}), 404

    return 204


@app.route(basePath+'/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    success = items_repository.delete(item_id)

    if not success:
        return jsonify({"error": "Item not found"}), 404

    return 204