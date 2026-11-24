import pytest

from app import app, load_products


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_csv_contains_at_least_twenty_products():
    products = load_products()

    assert len(products) >= 20
    assert {"id", "name", "category", "price", "stock"} <= products[0].keys()


def test_home_page_returns_ok(client):
    response = client.get("/")

    assert response.status_code == 200


def test_product_listing_displays_name_category_price_and_stock(client):
    response = client.get("/products")

    assert response.status_code == 200
    assert b"Classic T-Shirt" in response.data
    assert b"Clothing" in response.data
    assert b"$19.99" in response.data
    assert b"Stock: 48" in response.data


def test_search_matches_partial_product_names(client):
    response = client.get("/products?search=running")

    assert response.status_code == 200
    assert b"Running Shoes" in response.data
    assert b"Classic T-Shirt" not in response.data


def test_category_filter_only_shows_matching_products(client):
    response = client.get("/products?category=Footwear")

    assert response.status_code == 200
    assert b"Running Shoes" in response.data
    assert b"Travel Backpack" not in response.data


def test_search_and_category_filters_can_be_combined(client):
    response = client.get("/products?search=shoes&category=Footwear")

    assert response.status_code == 200
    assert b"Running Shoes" in response.data
    assert b"Classic T-Shirt" not in response.data
