from cryptography.fernet import Fernet

master_pwd = input("Enter your password: ")
key = Fernet.generate_key()
fernet = Fernet(key)


def write_key():
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("key.key", "rb").read()


key = load_key() + master_pwd.encode()
fernet = Fernet(key)


def view():
    with open("passwords.txt") as f:
        for line in f.readlines():
            data = line.rstrip()
            name, pwd = data.split("|")
            print("Name:", name, "| Password:", fernet.decrypt(pwd.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fernet.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("would you like to add password or view password(view, add)")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode")
        continue
