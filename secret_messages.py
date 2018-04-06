import utils
from caesar import Caesar
from keyword_c import KeywordCipher
from bifid import Bifid

if __name__ == "__main__":

    # inputs
    selected_cipher = ''
    selected_action = ''
    message = ''
    cipher_obj = None

    utils.show_options()

    while not utils.check_selection(selected_cipher):
        selected_cipher = utils.request_option()

    message = input("That's an excellent cipher. What's the message? ")

    while not utils.check_action(selected_action):
        selected_action = utils.request_action()

    if selected_cipher == "Caesar":
        cipher_obj = Caesar()
        print(utils.process_encryption(cipher_obj, message, selected_action))
    elif selected_cipher == "Keyword":
        keyword = input("Enter your keyword: ")
        cipher_obj = KeywordCipher(keyword)
        print(utils.process_encryption(cipher_obj, message, selected_action))
    elif selected_cipher == "Bifid":
        keyword = input("Enter your keyword: ")
        cipher_obj = Bifid(keyword)
        print("This is your encoded message:")
        print(utils.process_encryption(cipher_obj, message, selected_action))
