"""Mailroom: commandline tool to generate donor reports and emails."""

import sys

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

if sys.version_info[0] == 3:
    raw_input = input


def main():
    """Redirect the user to functions based on input."""
    input_prompt = """
    1. Send a Thank You Email
    2. View Donor Report
    3. Quit
    """
    user_input = raw_input(input_prompt)

    while True:
        if user_input == '1':
            donor_name = raw_input('Enter donor name or type "list" to show full donor list\n')
            result = ask_donor_name(donor_name)
            # if len(str(result)) > 1:
            #     user_input = result[0]
            #     name = result[1]
            # else:
            #     user_input = result
            user_input = result
            continue
        elif user_input == 'donate':
            money_amt = raw_input('Enter amount of donation:\n')
            name = donor_name
            user_input = ask_donation_amount(name, money_amt)
            continue
        elif user_input == 'initial':
            user_input = raw_input(input_prompt)
            continue
        elif user_input == '2':
            print(create_donor_report())
            user_input = 'initial'
            continue
        elif user_input == '3':
            KeyboardInterrupt
        # else:
        #     print('Please enter valid input.')
        #     user_input = 'initial'
        #     continue


def ask_donor_name(name):
    """Prompt user for donor's name, add to database if new donor"""
    if name == 'list':
        for donor in DONOR_DICT:
            print(donor)
        return '1'
    elif name in DONOR_DICT:
        return 'donate'
    elif name not in DONOR_DICT:
        DONOR_DICT[name] = []
        return 'donate'
    elif name.lower() == 'quit':
        KeyboardInterrupt


def ask_donation_amount(donor_name, donor_amount):
    """Prompt user for donor's donation amount, add to DB, send email."""
    if donor_amount.lower() == 'quit':
        KeyboardInterrupt
    elif int(donor_amount) <= 0:
        print('Invalid input. Enter a numerical value greater than zero. \n')
        return 'donate'
    else:
        DONOR_DICT[donor_name].append(donor_amount)

        formatted_thankyou_email = """
        Dear {},

        On behalf of the Ramson-Dole Foundation for Children Who Can't Read
        Good, we would like to personally thank you for your generous donation
        of ${}. Your donation will go directly to providing school supplies,
        tutors, and textbooks for children in the Seattle area.

        Thank you for your generosity!

        Sincerely,

            Chelsea Dole and Kinley Ramson
            Founders, Ramson-Dole Foundation
        """
        print(formatted_thankyou_email.format(donor_name, donor_amount))
        print('Your email to {} has been sent!'.format(donor_name))
        return 'initial'


def create_donor_report():
    """Create donor report."""
    print("--Ramson-Dole Foundation Donor Report--")

    print("""Donor Name   |   Total Donated  |   # of Donations  |  Average Donation
    """)

    for key, value in DONOR_DICT.items():
        donor_name = key
        total_don = sum(value)
        num_dons = len(value)
        avg_don = round(sum(value) / len(value))
        print('{}       {}            {}          {}'.format(donor_name, total_don, num_dons, avg_don))

    return 'initial'
