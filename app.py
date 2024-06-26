from flask import Flask, request, jsonify
from products import Products
from orders import Orders

# Create Flask instance
app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Mini Shop API!"

# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({'data': Products})

# Get a single product by product_id
@app.route('/products/id/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = next((product for product in Products if product['product_id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"message": "Product not found"}), 404

# Get a product by name
@app.route('/products/name/<name>', methods=['GET'])
def get_product_by_name(name):
    product = next((product for product in Products if product['name'] == name), None)
    if product:
        return jsonify(product)
    return jsonify({"message": "Product not found"}), 404

# Get products by availability
@app.route('/products/availability/<availability>', methods=['GET'])
def get_products_by_availability(availability):
    available_products = [product for product in Products if product['availability'] == availability]
    if available_products:
        return jsonify({'data': available_products})
    return jsonify({"message": "No products found with availability status"}), 404

# Update a product by name
@app.route('/products/name/<name>', methods=['PUT'])
def update_product(name):
    product = next((product for product in Products if product['name'] == name), None)
    if not product:
        return jsonify({'message': "Product not found"}), 404
    data = request.get_json()
    product.update(data)
    return jsonify(product)

# Create a new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = {
        'product_id': len(Products) + 1,
        'name': data.get('name'),
        'price': data.get('price'),
        'description': data.get('description'),
        'availability': data.get('availability')
    }
    Products.append(new_product)
    return jsonify(new_product), 201

# Delete a product by name
@app.route('/products/name/<name>', methods=['DELETE'])
def delete_product(name):
    product = next((product for product in Products if product['name'] == name), None)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    Products.remove(product)
    return jsonify({"message": "Product deleted"}), 200

# Create an order
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = {
        'order_id': len(Orders) + 1,
        'product_id': data.get('product_id'),
        'name': data.get('name'),
        'availability': data.get('availability'),
        'quantity': data.get('quantity')
    }
    Orders.append(new_order)
    return jsonify(new_order), 201

# Get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify({'data': Orders})

# Get a single order by order_id
@app.route('/orders/id/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    order = next((order for order in Orders if order['order_id'] == order_id), None)
    if order:
        return jsonify(order)
    return jsonify({"message": "Order not found"}), 404

# Get orders by product name
@app.route('/orders/name/<name>', methods=['GET'])
def get_orders_by_product_name(name):
    product_orders = [order for order in Orders if order['name'] == name]
    if product_orders:
        return jsonify({'data': product_orders})
    return jsonify({"message": "No orders found for the product"}), 404

# Cancel an order
@app.route('/orders/id/<int:order_id>', methods=['DELETE'])
def cancel_order(order_id):
    order = next((order for order in Orders if order['order_id'] == order_id), None)
    if not order:
        return jsonify({"message": "Order not found"}), 404
    Orders.remove(order)
    return jsonify({"message": "Order cancelled"}), 200

# Start the server
if __name__ == '__main__':
    app.run()
