class AdditiveCipher:
    def __init__(self, text = ""):
        self.text = text
        self.shift = 0

    def encrypt(self, shift):
        self.shift = shift
        for i in range(len(self.text)):
            if self.text[i].islower():
                self.text = self.text[:i] + chr((((ord(self.text[i]) - 97) + self.shift) % 26) + 97) + self.text[i + 1:]
            elif self.text[i].isupper():
                self.text = self.text[:i] + chr((((ord(self.text[i]) - 65) + self.shift) % 26) + 65) + self.text[i + 1:]

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

