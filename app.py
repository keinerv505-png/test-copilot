import csv
from pathlib import Path

from flask import Flask, render_template, request


BASE_DIR = Path(__file__).resolve().parent
PRODUCTS_FILE = BASE_DIR / "data" / "products.csv"

app = Flask(__name__)


def load_products():
    with PRODUCTS_FILE.open(newline="", encoding="utf-8") as csv_file:
        products = list(csv.DictReader(csv_file))
    for product in products:
        product["price"] = float(product["price"])
    return products


@app.route("/products")
@app.route("/")
def products():
    all_products = load_products()
    categories = sorted({product["category"] for product in all_products})
    search_term = (request.args.get("search") or request.args.get("q", "")).strip()
    requested_category = request.args.get("category", "").strip()
    selected_category = next(
        (
            category
            for category in categories
            if category.casefold() == requested_category.casefold()
        ),
        "",
    )

    filtered_products = all_products
    if search_term:
        search_key = search_term.casefold()
        filtered_products = [
            product
            for product in filtered_products
            if search_key in product["name"].casefold()
        ]
    if selected_category:
        filtered_products = [
            product
            for product in filtered_products
            if product["category"] == selected_category
        ]

    return render_template(
        "products.html",
        products=filtered_products,
        categories=categories,
        search_term=search_term,
        selected_category=selected_category,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
