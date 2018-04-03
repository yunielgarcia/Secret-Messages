from cipher import Cipher
import utils


if __name__ == "__main__":

    # inputs
    selected_cipher = ''
    message = ''

    utils.show_options()

    while not utils.check_selection(selected_cipher):
        selected_cipher = utils.request_option()

    message = input("That's an excellent cipher. What's the message? ")

    action_option = input("")