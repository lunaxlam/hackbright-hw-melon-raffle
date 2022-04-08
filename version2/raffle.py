"""Randomly pick customer and print customer info"""

import random

from customers import get_customers_from_file


def get_random_customer(customers):
    """Randomly pick a customer and return the customer."""

    customer = random.choice(customers)

    return customer


def print_customer_info(customer):
    """Print info about a chosen customer."""

    name = customer.name
    email = customer.email
    street = customer.street
    city = customer.city
    zipcode = customer.zipcode

    print(f"Customer name: {name}, Email: {email}, Street: {street}, City: {city}, Zipcode: {zipcode}")

    
def main():
    """Call the program's functions."""

    # Call function to get a list of customers
    customers = get_customers_from_file("customers.txt")
    # Call a function to get a random customer
    customer = get_random_customer(customers)
    print_customer_info(customer)


# If the file that we are running is the main program file then call run_raffle()
if __name__ == "__main__":
    main()

