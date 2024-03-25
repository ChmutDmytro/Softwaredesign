class Authenticator:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._logged_in_users = set()  # Початкове значення для списку залогінених користувачів
        return cls._instance

    def login(self, username):
        self._logged_in_users.add(username)
        print(f"User '{username}' logged in.")

    def logout(self, username):
        if username in self._logged_in_users:
            self._logged_in_users.remove(username)
            print(f"User '{username}' logged out.")
        else:
            print(f"User '{username}' is not logged in.")

    def get_logged_in_users(self):
        return self._logged_in_users


def main():
    auth1 = Authenticator()
    auth2 = Authenticator()

    auth1.login("user1")
    auth2.login("user2")

    print(auth1.get_logged_in_users())
    print(auth2.get_logged_in_users())

    auth1.logout("user1")
    print(auth1.get_logged_in_users())

if __name__ == "__main__":
    main()
