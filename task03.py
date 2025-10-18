class User:
    def __init__(self, username, email, is_active):
        self.username = username
        self.email = email
        self.is_active = is_active
user1 = User("miyasar", "miiassarm@gmail.com", True)
user2 = User("sabina", "sabinam@gmail.com", False)
user3 = User("sarvinoz", "sarvi2004@gamil.com", True)
print(user1.username, user1.email, user1.is_active)
print(user2.username, user2.email, user2.is_active)
print(user3.username, user3.email, user3.is_active)