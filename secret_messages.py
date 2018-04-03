from cipher import Cipher
import utils


if __name__ == "__main__":

    # inputs
    selected_cipher = ''
    selected_action = ''
    message = ''

    utils.show_options()

    while not utils.check_selection(selected_cipher):
        selected_cipher = utils.request_option()

    message = input("That's an excellent cipher. What's the message? ")

    while not utils.check_action(selected_action):
        selected_action = utils.request_action()

    print(selected_action, selected_cipher, message)