from affineCipher import Affine

def main():
    option = 1
    cipher = Affine()
    while option != 3:
        print("1. Encrypt a Text")
        print("2. Decrypt an encrypted Text")
        print("3. Exit")
        option = int(input("Enter: "))
        if option == 1:
            text = input("Enter a Text: ")
            cipher = Affine(text)
            cipher.encrypt()
            print("Encrypted Text:", cipher)
        elif option == 2:
            text = input("Enter a Text (Leave Empty to use previously encrypted Text): ")
            cipher.decrypt(text)
            print("Decrypted Text:", cipher)
        elif option != 3:
            print("Wrong option!")


if __name__ == "__main__":
    main()