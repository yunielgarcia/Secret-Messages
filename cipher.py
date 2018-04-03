class Cipher:
    _actions = "encrypt", "decrypt"

    def __init__(self):
        pass

    def encrypt(self, message):
        raise NotImplementedError()

    def decrypt(self, message):
        raise NotImplementedError()

    @classmethod
    def action_calls(cls):
        return cls._actions

