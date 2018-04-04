class Cipher:
    _actions = "encrypt", "decrypt"

    def __init__(self):
        pass

    def encrypt(self, message):
        """Apply the selected encryption method to the message
        @:param message
        :returns: encrypted message string"""
        raise NotImplementedError()

    def decrypt(self, message):
        """Apply the selected decryption method to the encrypted message
        :param message:
        :return:
        """
        raise NotImplementedError()

    @classmethod
    def action_calls(cls):
        return cls._actions

