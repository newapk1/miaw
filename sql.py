import sqlite3

def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        print("Login successful")
    else:
        print("Login failed")

def register_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
    conn.commit()
    print(f"User {username} registered successfully!")

def vulnerable_input():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"Hello {name}, you are {age} years old.")

def weak_authentication():
    user_input = input("Enter your username: ")
    if user_input == 'admin':
        print("Welcome admin!")
    else:
        print("Access denied!")

def main():
    print("Welcome to the system!")
    login('test_user', 'password123')
    register_user('new_user', '1234')
    vulnerable_input()
    weak_authentication()

if __name__ == "__main__":
    main()
