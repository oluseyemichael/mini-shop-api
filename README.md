# Mini Shop API

This is a simple mini shop API built using Flask. It allows users to manage products and orders for a shop. The API supports CRUD operations for products and order management including creating, retrieving, updating, and deleting orders.

## Features

- Retrieve a list of all products
- Get details of a specific product by ID or name
- Add a new product
- Update an existing product
- Delete a product
- Create a new order
- Retrieve a list of all orders
- Get details of a specific order by ID or product name
- Cancel an order

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Postman (for testing)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/oluseyemichael/mini-shop-api.git
    cd mini-shop-api
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Start the Flask server:**

    ```bash
    python app.py
    ```

2. **Access the API at:**

    ```
    http://127.0.0.1:5000
    ```

### API Endpoints

#### Products

- **Get All Products**
  - **Method:** GET
  - **URL:** `/products`
  - **Description:** Retrieve a list of all products available for sale.

- **Get Product by ID**
  - **Method:** GET
  - **URL:** `/products/id/<int:product_id>`
  - **Description:** Get the details of a specific product by its ID.

- **Get Product by Name**
  - **Method:** GET
  - **URL:** `/products/name/<string:name>`
  - **Description:** Get the details of a specific product by its name.

- **Get Products by Availability**
  - **Method:** GET
  - **URL:** `/products/availability/<string:availability>`
  - **Description:** Get the products filtered by availability status.

- **Create a New Product**
  - **Method:** POST
  - **URL:** `/products`
  - **Description:** Add a new product to the shop.
  - **Body:** JSON
    ```json
    {
      "name": "Shampoo",
      "price": 150,
      "description": "A hair care product used to clean the hair.",
      "availability": "available"
    }
    ```

- **Update an Existing Product**
  - **Method:** PUT
  - **URL:** `/products/name/<string:name>`
  - **Description:** Update the details of an existing product by its name.
  - **Body:** JSON
    ```json
    {
      "product_id": 1,
      "name": "Brush",
      "price": 120,
      "description": "A grooming tool used to clean, style, and maintain the appearance of human hair.",
      "availability": "available"
    }
    ```

- **Delete a Product**
  - **Method:** DELETE
  - **URL:** `/products/name/<string:name>`
  - **Description:** Delete a product by its name.

#### Orders

- **Create an Order**
  - **Method:** POST
  - **URL:** `/orders`
  - **Description:** Create a new order for a product.
  - **Body:** JSON
    ```json
    {
      "product_id": 1,
      "name": "Brush",
      "availability": "available",
      "quantity": 10
    }
    ```

- **Get All Orders**
  - **Method:** GET
  - **URL:** `/orders`
  - **Description:** Retrieve a list of all orders.

- **Get Order by ID**
  - **Method:** GET
  - **URL:** `/orders/id/<int:order_id>`
  - **Description:** Get the details of a specific order by its ID.

- **Get Orders by Product Name**
  - **Method:** GET
  - **URL:** `/orders/name/<string:name>`
  - **Description:** Get the orders filtered by product name.

- **Cancel an Order**
  - **Method:** DELETE
  - **URL:** `/orders/id/<int:order_id>`
  - **Description:** Cancel an order by its ID.

### Postman Collection

You can import and run the API requests in Postman using the following link:

[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://god.gw.postman.com/run-collection/24581384-64518a9f-66f6-4c6f-9ec4-d60b40a68db1?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D24581384-64518a9f-66f6-4c6f-9ec4-d60b40a68db1%26entityType%3Dcollection%26workspaceId%3D424bed35-fadb-4d26-856e-05f470cb0330)

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
