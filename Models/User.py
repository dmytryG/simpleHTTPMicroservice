from Models.Serializable import Serializable


class User(Serializable):
    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password
        