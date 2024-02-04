import hashlib


class User:
    id_count = 0

    def __init__(self, login, password, *args, **kwargs):
        self._login = login
        self._password = hashlib.sha256(password.encode()).hexdigest()
        self._id = f"@{str(self._login)}{str(User.id_count)}"
        User.id_count += 1


    def __repr__(self):
        return f"name:{self._login},password:{self._password},id:{self._id}"

    @classmethod
    def create_user(cls):
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        return cls(username, password)

    def add_name(self, username):
        self._login = username
        return self._login

    def get_name(self):
        return self._login

    def get_password(self):
        return self._password

    def get_id(self):
        return self._id

    def to_dict(self):
        return {'name': self._login, "id": self._id, 'password': self._password}

    @classmethod
    def from_dict(cls, user_dict):
        return cls(user_dict['name'], user_dict['password'], user_dict['id'])



