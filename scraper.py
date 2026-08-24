import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd


# Website URL
URL = "https://books.toscrape.com/"


# Request headers
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


# Send request to website
response = requests.get(
    URL,
    headers=HEADERS,
    timeout=10
)


# Check whether website is accessible
if response.status_code == 200:

    print("Website connected successfully!")

    # Parse homepage HTML
    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    # Find all products
    products = soup.select(
        "article.product_pod"
    )

    print(f"Products found: {len(products)}")
    print("=" * 70)


    # Store scraped products
    product_data = []


    # Process every product
    for product in products:

        # --------------------------------
        # PRODUCT TITLE
        # --------------------------------

        title = product.h3.a["title"]


        # --------------------------------
        # PRODUCT PRICE
        # --------------------------------

        price = product.select_one(
            ".price_color"
        ).text.strip()

        # Fix pound symbol encoding
        try:
            price = price.encode(
                "latin1"
            ).decode(
                "utf-8"
            )
        except UnicodeEncodeError:
            pass


        # --------------------------------
        # PRODUCT RATING
        # --------------------------------

        rating_element = product.select_one(
            ".star-rating"
        )

        if rating_element:

            rating_classes = rating_element.get(
                "class"
            )

            rating = rating_classes[1]

        else:

            rating = "Not Rated"


        # --------------------------------
        # PRODUCT URL
        # --------------------------------

        product_link = product.h3.a.get(
            "href"
        )

        product_url = urljoin(
            URL,
            product_link
        )


        # --------------------------------
        # PRODUCT DETAIL PAGE
        # --------------------------------

        detail_response = requests.get(
            product_url,
            headers=HEADERS,
            timeout=10
        )


        # Default description
        description = "Not Available"


        # --------------------------------
        # EXTRACT DESCRIPTION
        # --------------------------------

        if detail_response.status_code == 200:

            detail_soup = BeautifulSoup(
                detail_response.text,
                "html.parser"
            )

            description_heading = detail_soup.find(
                "div",
                id="product_description"
            )

            if description_heading:

                description_element = (
                    description_heading.find_next("p")
                )

                if description_element:

                    description = (
                        description_element
                        .get_text(
                            " ",
                            strip=True
                        )
                    )

                    # Fix incorrectly decoded UTF-8
                    # characters such as â and â
                    try:

                        description = (
                            description
                            .encode("latin1")
                            .decode("utf-8")
                        )

                    except UnicodeEncodeError:

                        pass


        # --------------------------------
        # STORE PRODUCT
        # --------------------------------

        product_data.append(
            {
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Description": description,
                "URL": product_url
            }
        )


        print(f"Scraped: {title}")


    # --------------------------------
    # CREATE DATAFRAME
    # --------------------------------

    df = pd.DataFrame(
        product_data
    )


    # --------------------------------
    # SAVE CSV
    # --------------------------------

    output_file = "data/products.csv"

    df.to_csv(
        output_file,
        index=False,
        encoding="utf-8-sig"
    )


    # --------------------------------
    # COMPLETION MESSAGE
    # --------------------------------

    print("=" * 70)
    print("Scraping completed successfully!")
    print(f"Total products: {len(df)}")
    print(f"Data saved to: {output_file}")


else:

    print(
        f"Failed to access website. "
        f"Status code: {response.status_code}"
    )
