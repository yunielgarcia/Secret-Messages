from cipher import Cipher

CIPHERS = ('Keyword', 'Caesar', 'Bifid', 'Atbash')


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


def request_action():
    """Display prompt asking what action to take. If not correct this function is reused"""
    selection = input("Are we going to encrypt or decrypt ")
    return selection


def check_action(action):
    """Check the correct action for the cipher,
    otherwise ask it again
    """
    return action in Cipher.action_calls()


def process_encryption(cipher, msg, action):
    if isinstance(cipher, Cipher):
        if action == "encrypt":
            return cipher.encrypt(msg)
        elif action == "decrypt":
            return cipher.decrypt(msg)
