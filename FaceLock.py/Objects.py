
class user:

    user_counter = 1

    def __init__(self, first, last, password, year):
        self.first = first
        self.last = last
        self.password = password
        self.year = year
        self.username = self.first + " " + self.last
        

        user.user_counter += 1
 
    def __str__(self):
        return f"Name: {self.username} \n Birthday: {self.year} \n Password: {self.password}"


# user_first = str(input("First name: "))
# user_last = input("Last name: ")
# user_year = input("Birthday: ")
# user_password = input("insert a password: ")

# user1 = user(user_first, user_last, user_password, user_year)

# print(user1)

user1 = user("Stefan", "Næss", "Stef", 2003)

