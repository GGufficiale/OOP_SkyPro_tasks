"""
Напишите класс User, имеющий следующие свойства и методы:

- __init__(self, name, password): конструктор, принимающий имя пользователя и пароль
- name: свойство, которое возвращает имя пользователя
- password: свойство, которое позволяет установить или изменить пароль пользователя
- is_admin: свойство, которое возвращает, является ли пользователь администратором или нет
- _is_admin: свойство-помощник, которое определяет, является ли пользователь администратором или нет
- login(self, password): метод, который проверяет, соответствует ли введенный пароль паролю пользователя
- logout(self): метод, который выходит из аккаунта пользователя (устанавливает значение свойства _is_logged_in в False при условии, что пользователь залогинен)

Для свойств name и password используйте декораторы @property и @password.setter.
"""


class User:
    def __init__(self, name, password):
        self._name = name
        self._password = password
        self.is_admin = False
        self._is_logged_in = False

    @property
    def name(self):
        return f'{self._name}'

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def _is_admin(self):
        return self._is_admin

    @_is_admin.setter
    def _is_admin(self, value):
        self.is_admin = value

    def login(self, password):
        if password == self._password:
            self._is_logged_in = True
            return True
        return False

    def logout(self):
        if self._is_logged_in:
            self._is_logged_in = False


# код для проверки
user1 = User("Alice", "qwerty")
print(user1.name)  # Alice
print(user1.password)  # qwerty
print(user1.is_admin)  # False

user1.password = "newpassword"
print(user1.password)  # newpassword

user1._is_admin = True
print(user1.is_admin)  # True

user1.login("newpassword")  # True
user1.logout()
