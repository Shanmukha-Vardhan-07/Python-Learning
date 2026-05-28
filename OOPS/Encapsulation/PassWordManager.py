class PasswordManager:
    def __init__(self,master_key):
        self._master_key=master_key
        self._passwords={}

    def set_password(self,website,password):
        self._passwords[website]=password
        print(f"Password saved for {website}")

    def get_password(self,website,master_key):
        if master_key==self._master_key:
            if website in self._passwords:
                return self._passwords[website]
            else:
                return "No Password found for this website"
        else:
            return "Access denied"

master = input("Create Master Key: ")

pm = PasswordManager(master)

while True:
    print("\n1. Save Password")
    print("2. Get Password")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        website = input("Enter website name: ")
        password = input("Enter password: ")
        pm.set_password(website, password)

    elif choice == "2":
        website = input("Enter website name: ")
        key = input("Enter master key: ")

        result = pm.get_password(website, key)
        print("Result:", result)

    elif choice == "3":
        print("Exiting Password Manager...")
        break

    else:
        print("Invalid Choice! Try again.")

        