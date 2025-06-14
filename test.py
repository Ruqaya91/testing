# Hardcoded credentials
stored_username = "admin"
stored_password = "1234"

# Get user input
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check credentials
if username == stored_username and password == stored_password:
    print("Login Successful")
else:
    print("Login Failed")
