"""Randomly pick customer and print customer info"""

import random

from customers import get_customers_from_file


def pick_winner(customers):
    """Randomly pick a winner from the list of customers and return the winner."""

    winner = random.choice(customers)

    return winner


def print_winner_info(customer):
    """Print info about a chosen customer."""

    name = customer.name
    email = customer.email
    city = customer.city

    print(f"{name} (email: {email}) from {city} is the winner!")

    
def main():
    """Call the program's functions."""

    # Call function to get a list of customers
    customers = get_customers_from_file("customers.txt")
    # Call a function to get a random customer
    winner = pick_winner(customers)
    print_winner_info(winner)


# If the file that we are running is the main program file then call run_raffle()
if __name__ == "__main__":
    main()

