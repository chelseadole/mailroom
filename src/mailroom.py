"""Mailroom: commandline tool to generate donor reports and emails."""


DONOR_DICT = {
    'Chelsea Dole': [3000, 500, 500, 1000],
    'Kinley Ramson': [5000, 100, 200, 50, 2000, 1500],
    'Nick Hunt-Walker': [500, 500, 250],
    'Jose Tello': [20, 50, 30],
    'Erik Matheson': [10000, 12000, 8000],
    'Carol Greene': [50, 100, 200, 120],
    'Holly Butterfield': [50],
    'Elaine Demaray': [200, 300, 90],
    'Olivia Ortiz': [600, 200],
    'Erendiz Tarakci': [80, 50, 75, 75, 75, 200, 300],
    'Moe Sakan': [200, 300, 500]
}


def initial_prompt():
    # Main menu: choose between sending an email, viewing a report, or exiting
    print("""

    Ramson-Dole Foundation Donor Database.
    Follow the prompt, or type 'Quit' to exit
    the program at any point.

    \n 1.Send Thank You Email
    \n 2.View Donor History Report
    \n 3.Exit/Quit
    """)

    initial_prompt_response = raw_input('Enter 1, 2, or 3')

    if initial_prompt_response == 1:
        ask_donor_name()
    elif initial_prompt_response == 2:
        create_donor_report()
    elif initial_prompt_response.lower() == 'quit':
        SystemExit
    else:
        print('\n Invalid choice. Please type 1, 2, or 3.')
        initial_prompt()


def ask_donor_name():
    # Prompt user for donor's name, add to database if new donor
    print("""

        Enter the full name of the donor \n OR \n Type 'list' to show a \
        list of donor names""")

    thankyou_response = raw_input('Donor Name:')

    if thankyou_response == 'list':
        print(DONOR_DICT.keys())
        ask_donor_name()
    elif thankyou_response in DONOR_DICT:
        ask_donation_amount(thankyou_response)
    elif thankyou_response not in DONOR_DICT:
        DONOR_DICT[thankyou_response] = []
        ask_donation_amount(thankyou_response)
    elif thankyou_response.lower() == 'quit':
        SystemExit


def ask_donation_amount(donor_name):
    # Prompt user for donor's donation amount and add
    # their donation amount to the DONOR_DICT database
    formatted_donation_prompt = 'Enter amount donated by {}'.format(donor_name)

    print(formatted_donation_prompt)

    donation_amount = raw_input('Donation:')

    if donation_amount.lower() == 'quit':
        SystemExit
    elif donation_amount <= 0 or type(donation_amount) != int:
        print('Invalid input. Enter a numerical value greater than zero.')
        ask_donation_amount()
    elif type(donation_amount) == int:
        DONOR_DICT[donor_name].append(donation_amount)
        send_thankyou_email(donor_name, donation_amount)


def send_thankyou_email(donor_name, donation_amount):
    # Format, create, and send 'Thank You' email to donor

    formatted_thankyou_email = """
        Dear {},

        On behalf of the Ramson-Dole Foundation for Children Who Can't Read \
        Good, we would like to personally thank you for your generous \
        donation of ${}. Your donation will go directly to providing school \
        supplies, tutors, and textbooks for children in the Seattle area.

        Thank you for your generosity!

        Sincerely,

            Chelsea Dole and Kinley Ramson
            Founders, Ramson-Dole Foundation
    """

    print(formatted_thankyou_email)
    initial_prompt()


def create_donor_report():
    print("--Ramson-Dole Foundation Donor Report--")

    print("""Donor Name   |   Total Donated  |   # of Donations  |  Average Donation
    """)

    for key, value in DONOR_DICT:
        donor_name = key
        total_don = sum(value)
        num_dons = len(value)
        avg_don = sum(value) / float(len(value))
        print('{} {} {} {}'.format(donor_name, total_don, num_dons, avg_don))

    initial_prompt()


