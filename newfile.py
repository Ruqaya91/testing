import hashlib

# Hash a password for storing
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register a new user
def register(username, password):
    with open("users.txt", "a") as f:
        f.write(f"{username}:{hash_password(password)}\n")
    print("User registered.")

# Verify login
def login(username, password):
    hashed = hash_password(password)
    try:
        with open("users.txt", "r") as f:
            for line in f:
                stored_user, stored_hash = line.strip().split(":")
                if username == stored_user and hashed == stored_hash:
                    print("Login Successful")
                    return
        print("Login Failed")
    except FileNotFoundError:
        print("No users registered yet.")

# Example usage:
print("1. Register\n2. Login")
choice = input("Choose (1 or 2): ")
uname = input("Username: ")
pwd = input("Password: ")

if choice == "1":
    register(uname, pwd)
elif choice == "2":
    login(uname, pwd)
else:
    print("Invalid choice")
