from additiveCipher import AdditiveCipher

def main():
   option = 1
   cipher = AdditiveCipher()
   while option != 3:
        print("1. Encrypt a Text")
        print("2. Decrypt an encrypted Text")
        print("3. Exit")
        option = int(input("Enter: "))
        if option == 1:
            text = input("Enter a Text: ")
            shift = int(input("Enter a shift value: "))
            cipher = AdditiveCipher(text)
            cipher.encrypt(shift = shift)
            print("Encrypted Text:", cipher)

        elif option == 2:
            text = input("Enter a Text (Leave Empty to use previously encrypted Text): ")
            shift = input("Enter a shift value (Leave Empty to use previous Shift): ")

            if len(text) == 0:
                if len(shift) == 0:
                    cipher.decrypt()
            else:
                cipher = AdditiveCipher()
                if len(shift) == 0:
                    cipher.decrypt(text)
                else:
                    cipher.decrypt(text, shift = int(shift))

            print("Decrypted Text:", cipher)

        elif option != 3:
            print("Invalid Option!")
    


if __name__ == "__main__":
    main()