def ticket_sales(TOTAL_TICKET):

    """
    Handling the sale of tickets.

    Parameters:
        TOTAL_TICKET (int): Total number of tickets.

    Variables:
        desired (int): The amount of tickets the buyer wants to buy.

    Logic:
        1. Ask the user the desired number of tickets.
        2. Enter a number between 1 and 4.
        3. Ensure the buyer cannot request more tickets than what is available.
        4. If valid, display the number of remaining tickets.
        5. If invalid, ask the user to enter a number between 1 and 4.

    Return:
        desired (int): The total number of tickets sold.
    """


    desired = 0

    # Loops until 20 tickets are sold
    while True:


        desired = int(input(
            f'There are {TOTAL_TICKET} tickets available. '
            f'How many are being sold with a max of 4? '))


        if 1<= desired <= 4:

            # Ensures that user can get more than 20 tickets
            if desired > TOTAL_TICKET:
                print(f'There are {TOTAL_TICKET} remaining.')
            else:


                return desired

        else:
                print(f'Enter a number between 1 and 4.')

def amount_sold(ticket_sales):

    """
    Handling the sale of tickets.

    Parameters:
        amount_sold (function): A function that takes the number of tickets sold.

    Variables:
        TOTAL_TICKET (int): Total number of tickets.
        buyers (accumulators): An accumulator for the total number of buyers.
        ticket_sold (accumulators): an accumulator for the total number of tickets sold.

    Logic:
        1. Initialize total tickets, ticket_sold and buyers.
        2. Set up accumulators for buyers and ticket_sold.
        3. Display the number of buyers.

    Return:
        buyers (accumulators): An accumulator for the total number of buyers.

    """

    TOTAL_TICKET = 10
    ticket_sold = 0
    buyers = 0

    # Loops until all tickets are sold
    while TOTAL_TICKET > 0:

        desired = ticket_sales(TOTAL_TICKET)

        ticket_sold += desired

        TOTAL_TICKET -= desired

        buyers += 1
        print(f'There are {TOTAL_TICKET} remaining.')

    print(f'All the tickets were sold with {buyers} buyers.')

if __name__ == "__main__":
    amount_sold(ticket_sales)