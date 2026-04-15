from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product Catalog API"}), 200

@app.route("/products")
def get_products():
    category = request.args.get("category", default=None, type=str)
    
    if category:
        cat_lower = category.lower()
        filtered = [p for p in products if p["category"].lower() == cat_lower]
        return jsonify(filtered), 200

    return jsonify(products), 200


@app.route("/products/<int:id>")
def get_product_by_id(id):
    product = next((p for p in products if p["id"] == id), None)

    if product is None:
        return (
            jsonify(
                {
                    "error": "Not Found",
                    "message": f"Product with id {id} does not exist",
                }
            ),
            404,
        )

    return jsonify(product), 200
    

if __name__ == "__main__":
    app.run(debug=True)
