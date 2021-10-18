class AdditiveCipher:
    def __init__(self, text = ""):
        self.text = text
        self.shift = 0

    def encryptChar(self, char):
        if char.islower():
            return chr((((ord(char) - 97) + self.shift) % 26) + 97)
        elif char.isupper():
            return chr((((ord(char) - 65) + self.shift) % 26) + 65)

    def encrypt(self, shift):
        self.shift = shift
        self.text = "".join(map(self.encryptChar, self.text))

    def decrypt(self, text = "", shift = 0):

        if len(text) != 0:
            self.text = text
        self.shift = shift

        if self.shift != 0:
            shift = 26 - self.shift
            self.encrypt(shift)
            # reset shift
            self.shift = 0

    def __str__(self):
        return self.text

