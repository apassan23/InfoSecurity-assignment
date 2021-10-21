class Affine:
    def __init__(self, text = ""):
        self.text = text
        self.KEY = {"a": 17, "b": 20, "a_inv": 23}

    def encryptChar(self, char):
        # E(x) = (a*x + b) % 26
        return chr((((self.KEY.get("a") * ord(char)) + self.KEY.get("b")) % 26) + 65)

    def encrypt(self):
        self.text = "".join(map(self.encryptChar, self.text))

    def decryptChar(self, char):
        # D(x) = a^-1 * (x - b) % 26
        return chr((self.KEY.get("a_inv") * (ord(char) - self.KEY.get("b"))) % 26 + 65)

    def decrypt(self, text = ""):
        if len(text) == 0:
            self.text = "".join(map(self.decryptChar, self.text))
        else:
            self.text = "".join(map(self.decryptChar, text))

    def __str__(self):
        return self.text