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
        send_thankyou_email()
    elif initial_prompt_response == 2:
        create_donor_report()
    elif initial_prompt_response.lower() == 'quit':
        SystemExit
    else:
        print('\n Invalid choice. Please type 1, 2, or 3.')
        initial_prompt()


def send_thankyou_email():
    print("""

        Enter the full name of the donor to email, or type 'list' to \
        show a list of donor names.

    """)

    thankyou_response = raw_input('Donor Name:')

    if thankyou_response == 'list':
        print(DONOR_DICT.keys())
        send_thankyou_email()
    elif thankyou_response in DONOR_DICT:
        ask_donation_amount(thankyou_response)
    elif thankyou_response not in DONOR_DICT:
        DONOR_DICT[thankyou_response] = []
        ask_donation_amount(thankyou_response)
    elif thankyou_response.lower() == 'quit':
        SystemExit




















