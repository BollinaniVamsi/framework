# A list to store registered users
import pdb
pdb.set_trace()
users = []

# Function to register a new user
def register_user(username):
    if username not in users:
        users.append(username)
        print(f"User '{username}' has been registered successfully.")
    else:
        print(f"User '{username}' already exists.")

# Registering multiple users using a loop
num_users = 5  # You can adjust the number of users to register

for i in range(num_users):
    username = input(f"Enter username for user {i+1}: ")
    register_user(username)

# Testing user existence
while True:
    test_user = input("\nEnter username to check if it exists (or 'quit' to stop): ")
    if test_user == 'quit':
        break
    elif test_user in users:
        print(f"User '{test_user}' exists.")
    else:
        print(f"User '{test_user}' does not exist. Please register.")
        register_user(test_user)
