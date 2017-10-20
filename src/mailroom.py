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
    1.Send Thank You Email
    2.View Donor Report
    3.Exit/Quit
    """)

    initial_response = raw_input("What would you like to do? ") 

    if initial_response == 1: 
      send_thankyou_email()
    elif initial_response == 2:
      create_donor_report()
    elif initial_response == 3:
      # EXIT PROGRAM
    else:
      print('\n Invalid choice. Please type 1, 2, or 3.') 
      initial_prompt()