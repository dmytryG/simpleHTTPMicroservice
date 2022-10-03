class Response():
    def __init__(self, is_err: bool, data):
        self.is_err = is_err
        self.data = data