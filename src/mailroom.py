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

def get_input(prompt, options=None):
    print(prompt)
    response = raw_input(options)
    if options is None or response in options:
        return response
    else:
        print('Please enter valid response.')
        return get_input(prompt, options)

input_prompt = """
    \n 1.Send Thank You Email
    \n 2.View Donor History Report
    \n 3.Exit/Quit

    Enter 1, 2, or 3:
    """


donor_name_prompt = "Enter the full name of the donor -OR- 'list' to show a list of donors"


def mailroom():

    while True:

        menu_input = get_input(input_prompt, [1, 2, 3, 'quit'])


        if menu_input == 1:
            donor_name = get_input(donor_name_prompt)
            real_donor = ask_donor_name()
            if donor_name == 'ask donation':
                donation_amount = get_input('Enter amount donated:  ')
            # donor_name = get_input(donor_name_prompt)
            # if donor_name == 'list':
            #     for donor in DONOR_DICT:
            #         print(donor)
            #     donor_name = get_input(donor_name_prompt)
            # elif 
        

def ask_donor_name():
    # Prompt user for donor's name, add to database if new donor
    if thankyou_response == 'list':
        for donor in DONOR_DICT:
            print(donor)
        ask_donor_name()
    elif thankyou_response in DONOR_DICT:
        return 'ask donation'
    elif thankyou_response not in DONOR_DICT:
        DONOR_DICT[thankyou_response] = []
        return 'ask donation'
    elif thankyou_response.lower() == 'quit':
        KeyboardInterrupt


def ask_donation_amount(donor_name):
    # Prompt user for donor's donation amount and add
    # their donation amount to the DONOR_DICT database

    print(formatted_donation_prompt)

    if donation_amount.lower() == 'quit':
        KeyboardInterrupt
    elif int(donation_amount) <= 0 or type(donation_amount) == str:
        print('Invalid input. Enter a numerical value greater than zero. \n')
        ask_donation_amount(donor_name)
    else:
        DONOR_DICT[donor_name].append(donation_amount)
        send_thankyou_email(donor_name, donation_amount)


def send_thankyou_email(donor_name, donation_amount):
    # Format, create, and send 'Thank You' email to donor

    formatted_thankyou_email = """
        Dear {},

        On behalf of the Ramson-Dole Foundation for Children Who Can't Read \
        Good, we would like to personally thank you for your generous donation
        of ${}. Your donation will go directly to providing school supplies,
        tutors, and textbooks for children in the Seattle area.

        Thank you for your generosity!

        Sincerely,

            Chelsea Dole and Kinley Ramson
            Founders, Ramson-Dole Foundation
    """

    print(formatted_thankyou_email.format(donor_name, donation_amount))
    print('Your email to {} has been sent!'.format(donor_name))
    initial_prompt()


def create_donor_report():
    print("--Ramson-Dole Foundation Donor Report--")

    print("""Donor Name   |   Total Donated  |   # of Donations  |  Average Donation
    """)

    for key, value in DONOR_DICT.items():
        donor_name = key
        total_don = sum(value)
        num_dons = len(value)
        avg_don = round(sum(value) / len(value))
        print('{}       {}            {}          {}'.format(donor_name, total_don, num_dons, avg_don))

    initial_prompt()


