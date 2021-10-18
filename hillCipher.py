class Hill:
    def __init__(self, text = ""):
        self.text = text

    def getKeyMatrix(self, key):
        keyMatrix = [[0] * 2 for _ in range(2)]
        k = 0
        for i in range(2):
            for j in range(2):
                keyMatrix[i][j] = ord(key[k]) - 65
                k += 1

        return keyMatrix


    def encryptRange(self, start):
        textVector = [(ord(c) - 65) for c in self.text[start: start + 2]]
        result = [0] * 2
        for i in range(2):
            for _ in range(1):
                sum = 0
                for k in range(2):
                    sum += (self.keyMatrix[i][k] * textVector[k]) % 26
                result[i] = sum % 26
        return "".join(map(lambda c: chr(c + ord('A')), result))

    def encrypt(self, key):
        if len(self.text) % 2 == 1:
            print("Warning: Text Length is not even..")
            print("Adding '$' at the end...")
            self.text += '$'

        self.keyMatrix = self.getKeyMatrix(key)

        for i in range(0, len(self.text), 2):
            self.text = self.text[:i] + self.encryptRange(i) + self.text[i + 2:]


    def modInverse(self, a, m):
            try:
                g = pow(a, -1, m)
                return g
            except ValueError:
                return -1

    def decryptRange(self, start, detInverse):
        textVector = [(ord(c) - 65) for c in self.text[start: start + 2]]
        result = [0] * 2
        for i in range(2):
            for _ in range(1):
                sum = 0
                for k in range(2):
                    sum += (self.keyMatrix[i][k] * textVector[k])
                result[i] = (sum * detInverse) % 26

        return "".join(map(lambda c: chr(c + ord('A')), result))


    def decrypt(self, text = "", key = ""):
        if len(key) != 0:
            self.keyMatrix = self.getKeyMatrix(key)

        determinant = (self.keyMatrix[0][0] * self.keyMatrix[1][1]) - (self.keyMatrix[0][1] * self.keyMatrix[1][0])

        if determinant == 0:
            print("Invalid Key!")
            return

        self.keyMatrix[0][0], self.keyMatrix[1][1] = self.keyMatrix[1][1] , self.keyMatrix[0][0]
        self.keyMatrix[0][1] = -self.keyMatrix[0][1] 
        self.keyMatrix[1][0] = -self.keyMatrix[1][0]

        detInverse = self.modInverse(determinant % 26, 26)
        if detInverse == -1:
            print("Invalid Key! Decrypted Message may be wrong!")

        if len(text) != 0:
            self.text = text
        
        for i in range(0, len(self.text), 2):
            self.text = self.text[:i] + self.decryptRange(i, detInverse) + self.text[i + 2:]
        

    def __str__(self):
        return self.text