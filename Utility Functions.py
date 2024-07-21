import getpass
from models import User

def create_account():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    user = User(username, password)
    user.save()
    print("Account created successfully!")

def login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    if User.authenticate(username, password):
        print("Login successful!")
        return True
    else:
        print("Invalid username or password!")
        return False
