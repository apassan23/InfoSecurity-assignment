from hillCipher import Hill

def main():
    option = 1
    cipher = Hill()
    while option != 3:
        print("1. Encrypt a Text")
        print("2. Decrypt an encrypted Text")
        print("3. Exit")
        option = int(input("Enter: "))
        if option == 1:
            text = input("Enter a Text: ")
            key = input("Enter a Key (4 Characters Long): ")
            if len(key) != 4: 
                print("Invalid Key!")
                continue
            cipher = Hill(text)
            cipher.encrypt(key)
            print("Encrypted Text:", cipher)
        elif option == 2:
            text = input("Enter a Text (Leave Empty to use previously encrypted Text): ")
            key = input("Enter a Key (Leave Empty to use previously encrypted Key): ")
            cipher.decrypt(text, key)
            print("Decrypted Text:", cipher)
        elif option != 3:
            print("Wrong option!")


if __name__ == "__main__":
    main()