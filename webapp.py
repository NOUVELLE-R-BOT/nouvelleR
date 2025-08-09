products = {
    "1": {
        "name": "TIGRE 🐯",
        "origin": "Hollanda",
        "description": "Qualité premium 🔥",
        "image": "img1.jpg",
        "prices": [70, 180, 250, 400]
    },
    "2": {
        "name": "PINK 🦋",
        "origin": "Hollanda",
        "description": "Saveur douce & fruitée 🍓",
        "image": "img2.jpg",
        "prices": [80, 190, 260, 410]
    }
}

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
from flask import request

@app.route("/product")
def product_page():
    product_id = request.args.get("id")
    product = products.get(product_id)
    if not product:
        return "Produit introuvable", 404
    return render_template("product.html", product=product)


def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
