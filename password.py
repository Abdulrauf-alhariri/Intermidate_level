import random
import string


class GeneratePassword:

    def __init__(self, length, down_letters, num, upp_letters):
        self.length = length
        self.down_letters = down_letters
        self.num = num
        self.upp_letters = upp_letters

    @classmethod
    def weigh(cls):
        length = input("Eneter the length of your password:")
        print("")
        letters = input("Do you want lowercase (y/n)?").lower()
        print("")
        num = input("Do you want numbers (y/n)?").lower()
        print("")
        upp_letters = input("Do you want uppercase (y/n)?").lower()
        return cls(int(length), letters, num, upp_letters)

    def create_password(self):
        lenght = self.length
        if self.down_letters == "y" and self.upp_letters == "y" and self.num == "y":
            letters_numbers = string.ascii_letters + string.digits

        elif self.upp_letters == "y" and self.down_letters == "n" and self.num == "y":
            letters_numbers = string.ascii_uppercase + string.digits

        elif self.upp_letters == "n" and self.down_letters == "y" and self.num == "y":
            letters_numbers = string.ascii_lowercase + string.digits

        elif self.upp_letters == "n" and self.down_letters == "n" and self.num == "y":
            letters_numbers = string.digits

        my_password = random.choices(letters_numbers, k=lenght)
        return "".join(my_password)


password = GeneratePassword.weigh()
print("")
print("Your password is: ", password.create_password())


# i = input("length:")
# a = int(i)
# hello = string.ascii_letters + string.digits
# password1 = random.choices(hello, k=a)
# print(password1)
