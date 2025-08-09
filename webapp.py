from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/product")
def product_page():
    product_id = request.args.get("id")
    product = products.get(product_id)
    if not product:
        return "Produit introuvable", 404
    return render_template("product.html", product=product)

if __name__ == "__main__":
    app.run(debug=True)
