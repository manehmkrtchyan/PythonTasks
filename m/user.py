class User:
    def __init__(self, name, id, email):
        self._name = name
        self._id = id
        self._email = email

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_id(self):
        return self._id

    def get_email(self):
        return self._email

    def set_email(self, new_email):
        self._email = new_email
