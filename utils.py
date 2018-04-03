from cipher import Cipher

CIPHERS = ('Alberti', 'Affine', 'Atbash')


def show_options():
    """Print ciphers available"""
    print("\n\n" + "This is the Secret Messages project for the Treehouse Techdegree." + "\n")
    print("These are the current available ciphers: " + "\n")

    for cipher in CIPHERS:
        print("-" + cipher)

    print()  # Just a new line


def request_option():
    """Display prompt asking option. If not correct this function is reused"""
    selection = input("Which cipher would you like to use? ")
    return selection


def check_selection(selection):
    """Check the correct selection from option displayed,
    otherwise ask it again
    """
    return selection in CIPHERS
