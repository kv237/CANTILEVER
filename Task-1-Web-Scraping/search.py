import pandas as pd


# Load product data
file_path = "data/products.csv"

df = pd.read_csv(file_path)


print("=" * 60)
print("        PRODUCT SEARCH")
print("=" * 60)


# Get search input
search_term = input(
    "Enter product name to search: "
).strip().lower()


# Search products
results = df[
    df["Title"]
    .str.lower()
    .str.contains(search_term, na=False)
]


# Display results
print("\nSearch Results")
print("=" * 60)


if results.empty:

    print("No products found.")

else:

    print(
        f"Found {len(results)} product(s):\n"
    )

    for _, product in results.iterrows():

        print(f"Title: {product['Title']}")
        print(f"Price: {product['Price']}")
        print(f"Rating: {product['Rating']}")
        print(
            f"Description: "
            f"{product['Description'][:200]}..."
        )
        print("-" * 60)
