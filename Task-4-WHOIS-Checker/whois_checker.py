import whois
import csv
import os
import re
from datetime import datetime


# ==========================================
# Configuration
# ==========================================

RESULTS_DIR = "results"

CSV_FILE = os.path.join(
    RESULTS_DIR,
    "whois_results.csv"
)


# ==========================================
# Format Normal WHOIS Values
# ==========================================

def format_value(value):
    """
    Convert WHOIS values into clean,
    readable text.
    """

    if value is None:
        return "Not Available"

    if isinstance(value, (list, tuple)):

        unique_values = []

        for item in value:

            item = str(item).strip()

            if item and item not in unique_values:
                unique_values.append(item)

        return ", ".join(unique_values)

    if isinstance(value, datetime):

        return value.strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    return str(value)


# ==========================================
# Format WHOIS Dates
# ==========================================

def format_date(value):
    """
    Format WHOIS date values.

    If multiple dates are returned,
    the first valid datetime is used.
    """

    if value is None:
        return "Not Available"

    if isinstance(value, (list, tuple)):

        for item in value:

            if isinstance(item, datetime):

                return item.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

        if len(value) > 0:
            return str(value[0])

        return "Not Available"

    if isinstance(value, datetime):

        return value.strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    return str(value)


# ==========================================
# Validate Domain
# ==========================================

def is_valid_domain(domain):
    """
    Validate a domain name before performing
    the WHOIS lookup.
    """

    # Maximum domain length
    if len(domain) > 253:
        return False

    # Domain must contain at least one dot
    if "." not in domain:
        return False

    # Basic domain pattern
    pattern = r"^(?=.{1,253}$)([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63}$"

    return bool(
        re.match(
            pattern,
            domain
        )
    )


# ==========================================
# WHOIS Lookup
# ==========================================

def lookup_domain(domain):
    """
    Perform WHOIS lookup for a domain.
    """

    try:

        result = whois.whois(domain)

        data = {
            "Domain": format_value(
                result.domain_name
            ),

            "Registrar": format_value(
                result.registrar
            ),

            "Creation Date": format_date(
                result.creation_date
            ),

            "Expiration Date": format_date(
                result.expiration_date
            ),

            "Name Servers": format_value(
                result.name_servers
            ),

            "Status": format_value(
                result.status
            )
        }

        return data

    except Exception as error:

        print(
            f"\nWHOIS lookup failed: {error}"
        )

        return None


# ==========================================
# Save Result to CSV
# ==========================================

def save_to_csv(data):
    """
    Save WHOIS information to CSV.
    """

    os.makedirs(
        RESULTS_DIR,
        exist_ok=True
    )

    file_exists = os.path.exists(
        CSV_FILE
    )

    with open(
        CSV_FILE,
        "a",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=data.keys()
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)


# ==========================================
# Save Result to TXT
# ==========================================

def save_to_txt(data):
    """
    Save WHOIS information to an
    individual TXT report.
    """

    os.makedirs(
        RESULTS_DIR,
        exist_ok=True
    )

    domain = data.get(
        "Domain",
        "unknown"
    )

    filename = (
        domain
        .lower()
        .replace(".", "_")
        .replace("/", "_")
        .replace(" ", "_")
    )

    txt_file = os.path.join(
        RESULTS_DIR,
        f"{filename}.txt"
    )

    with open(
        txt_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "WHOIS DOMAIN INFORMATION\n"
        )

        file.write(
            "=" * 60 + "\n\n"
        )

        for key, value in data.items():

            file.write(
                f"{key}: {value}\n\n"
            )

        file.write(
            "=" * 60 + "\n"
        )

    return txt_file


# ==========================================
# Display Result
# ==========================================

def display_result(data):
    """
    Display WHOIS information
    in a readable format.
    """

    print(
        "\n" + "=" * 60
    )

    print(
        "             WHOIS DOMAIN INFORMATION"
    )

    print(
        "=" * 60
    )

    for key, value in data.items():

        print(
            f"{key}: {value}"
        )

    print(
        "=" * 60
    )


# ==========================================
# Main Program
# ==========================================

def main():

    print(
        "=" * 60
    )

    print(
        "          WHOIS DOMAIN INFO CHECKER"
    )

    print(
        "=" * 60
    )

    domain = input(
        "Enter domain name: "
    ).strip()


    # ======================================
    # Empty Input
    # ======================================

    if not domain:

        print(
            "\nError: Domain name cannot be empty."
        )

        return


    # ======================================
    # Clean Input
    # ======================================

    domain = (
        domain
        .replace("https://", "")
        .replace("http://", "")
        .strip("/")
        .strip()
        .lower()
    )


    # ======================================
    # Validate Domain
    # ======================================

    if not is_valid_domain(domain):

        print(
            f"\nInvalid domain name: {domain}"
        )

        print(
            "Please enter a valid domain such as:"
        )

        print(
            "google.com"
        )

        print(
            "example.org"
        )

        print(
            "github.com"
        )

        return


    print(
        f"\nLooking up WHOIS information for: {domain}"
    )


    # ======================================
    # WHOIS Lookup
    # ======================================

    data = lookup_domain(
        domain
    )


    # ======================================
    # Lookup Failure
    # ======================================

    if data is None:

        print(
            "\nCould not retrieve WHOIS information."
        )

        print(
            "The domain may not exist, "
            "may be protected, or its WHOIS "
            "server may be unavailable."
        )

        return


    # ======================================
    # Display
    # ======================================

    display_result(
        data
    )


    # ======================================
    # Save CSV
    # ======================================

    save_to_csv(
        data
    )


    # ======================================
    # Save TXT
    # ======================================

    txt_file = save_to_txt(
        data
    )


    print(
        "\nWHOIS information saved to:"
    )

    print(
        CSV_FILE
    )

    print(
        "TXT report saved to:"
    )

    print(
        txt_file
    )


# ==========================================
# Program Entry Point
# ==========================================

if __name__ == "__main__":

    main()
