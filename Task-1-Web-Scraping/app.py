from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)

# CSV file location
DATA_FILE = "data/products.csv"


@app.route("/")
def home():

    # Load product data
    df = pd.read_csv(DATA_FILE)

    # Get search query
    search = request.args.get(
        "search",
        ""
    ).strip()

    # Search products
    if search:

        results = df[
            df["Title"]
            .str.lower()
            .str.contains(
                search.lower(),
                na=False
            )
        ]

    else:

        results = df

    # Convert DataFrame to records
    products = results.to_dict(
        orient="records"
    )

    return render_template(
        "index.html",
        products=products,
        search=search
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )
