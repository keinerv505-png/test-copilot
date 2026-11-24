# Flask Store

Simple Flask application that displays products from a CSV file.

## Features

- Product listing
- Product search by partial name
- Category filtering

## Tech Stack

- Python
- Flask
- Bootstrap
- CSV

## Run locally

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows, activate it with `.venv\Scripts\activate`.

2. Install dependencies and start the application:

   ```bash
   pip install -r requirements.txt
   python app.py
   ```

3. Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://127.0.0.1:5000/products](http://127.0.0.1:5000/products).

The catalog is loaded from `data/products.csv`. Search with `?search=value` and filter with `?category=value`. To run the automated tests, use:

```bash
pytest
```

## Run with Docker

```bash
docker build -t flask-store .
docker run --rm -p 5000:5000 flask-store
```

Then open [http://127.0.0.1:5000/products](http://127.0.0.1:5000/products).

## Future Enhancements

- SQLite
- SQLAlchemy
- REST API