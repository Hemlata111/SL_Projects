import string

class BasePasswordManager:
    def __init__(self):
        # List to store all old passwords
        self.old_passwords = []

    def get_password(self):
        """
        Returns the current password.
        The last item in old_passwords is considered current.
        """
        if not self.old_passwords:
            return None
        return self.old_passwords[-1]

    def is_correct(self, password):
        """
        Returns True if the provided password matches current password.
        """
        return password == self.get_password()


class PasswordManager(BasePasswordManager):

    def get_level(self, password=None):
        """
        Returns the security level of a password.
        If no password is provided, returns level of current password.
        """

        if password is None:
            password = self.get_password()

        if not password:
            return 0

        has_alpha = any(c.isalpha() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)

        # Level 2 → Alphanumeric + special characters
        if has_alpha and has_digit and has_special:
            return 2
        
        # Level 1 → Alphanumeric
        if has_alpha and has_digit:
            return 1
        
        # Level 0 → Only alphabets OR only numbers
        return 0


    def set_password(self, new_password):
        """
        Sets new password if:
        - Length >= 6
        - Security level is greater than current password
        - If current password is level 2 (highest),
          new password must also be level 2
        """

        if len(new_password) < 6:
            print("Password change failed: Minimum length is 6.")
            return False

        new_level = self.get_level(new_password)

        # If no password exists yet
        if not self.old_passwords:
            self.old_passwords.append(new_password)
            print("Password set successfully.")
            return True

        current_level = self.get_level()

        # If current password already highest level (2)
        if current_level == 2:
            if new_level == 2:
                self.old_passwords.append(new_password)
                print("Password updated successfully.")
                return True
            else:
                print("Password change failed: Must be highest security level.")
                return False

        # If new password has higher security level
        if new_level > current_level:
            self.old_passwords.append(new_password)
            print("Password updated successfully.")
            return True
        else:
            print("Password change failed: Security level not high enough.")
            return False
        
if __name__ == "__main__":
    pm = PasswordManager()

    while True:
        print("\n---- Password Manager ----")
        print("1. Set Password")
        print("2. Check Password")
        print("3. Get Current Password")
        print("4. Get Security Level")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if not choice.isdigit():
            print("Please enter a number between 1 and 5.")
            continue

        if choice == "1":
            new_pass = input("Enter new password: ")
            pm.set_password(new_pass)

        elif choice == "2":
            check_pass = input("Enter password to check: ")
            if pm.is_correct(check_pass):
                print("Password is correct ✅")
            else:
                print("Password is incorrect ❌")

        elif choice == "3":
            print("Current Password:", pm.get_password())

        elif choice == "4":
            print("Security Level:", pm.get_level())

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")