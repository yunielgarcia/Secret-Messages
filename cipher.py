class Cipher:
    _actions = "encrypt", "decrypt"

    def __init__(self):
        pass

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

    @classmethod
    def action_calls(cls):
        return cls._actions

