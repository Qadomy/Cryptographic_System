"""
Cryptographic system that implements encryption and decryption algorithms for:
Caesar Cipher
"""
class caesarCipher():

    alphabets = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l',
                12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x',
                24: 'y', 25: 'z'}

    """
    alphabetsUPPER = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
                      10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S',
                      19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

    """
    specChar = {0: "~", 1: ".", 2: "?", 3: ";", 4: ":", 5: "!", 6: "@", 7: "$", 8: "%", 9: "^",
                10: "&", 11: "(", 12: ")", 13: "+", 14: "-", 15: "*", 16: "/", 17: "<", 18: ">",
                19: "`", 20: "#", 21: "\"", 22: "'", 23: ","}

    numersS = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7', 7: '8', 8: '9', 9: '0'}

    """Read the text from the file"""
    def readFileText(self, filetext):
        file = open(filetext, 'r')
        plainText = file.read()
        file.close()

        return plainText

    """Check the special character in the text"""
    def isSpecialChar(self, element):
        for char in self.specChar:
            if (element == self.specChar[char]):
                return True
        return False

    """Check the character lowercase or uppercase in the text"""

    def isCharacter(self, element):
        for letter in self.alphabets:
            if (element.lower() == self.alphabets[letter]):
                return True
        return False

    """Check the numbers in the text"""
    def isNumber(self, element):
        for num in self.numersS:
            if (element == self.numersS[num]):
                return True
        return False


    """******************************************************"""

    """Encryptions the text"""
    def encrypt(self, textFile):
        keyFile = open('keyFile.txt')
        keyText = int(keyFile.read())

        string_output = ''

        for mElement in textFile:
            if (mElement == " "): # for the space
                string_output += " "

            elif (mElement == "."):
                string_output += "."

            elif (self.isSpecialChar(mElement)):
                for aCharacter in self.specChar:
                    if mElement == self.specChar[aCharacter]:
                        eChar = (aCharacter + keyText) % 24 # number of special characters
                        string_output += self.specChar[eChar]


            elif (self.isNumber(mElement)):
                for aNumber in self.numersS:
                    if mElement == self.numersS[aNumber]:
                        aNum = (aNumber + keyText) % 10
                        string_output += self.numersS[aNum]

            elif (self.isCharacter(mElement)):
                for aLetter in self.alphabets:
                    if(mElement.lower() == self.alphabets[aLetter]):
                        eLetter = (aLetter + keyText) % 26 # number of letters
                        string_output += self.alphabets[eLetter]
                    #elif(mElement)

            else:
                string_output += mElement

        import pickle

        print(string_output)
        pickle.dump(string_output, open("EncryptedFile.enc", 'wb'))


        encryptedFile = open("EncryptedFile.txt", "w")
        encryptedFile.write(string_output)
        encryptedFile.close()

    """******************************************************"""

    def decrypt(self, textFile):
        keyFile = open('keyFile.txt')
        keyText = int(keyFile.read())

        string_output = ''

        for mElement in textFile:
            if (mElement == " "):
                string_output += " "

            elif (mElement == "."):
                string_output += "."

            elif (self.isSpecialChar(mElement)):
                for aCharacter in self.specChar:
                    if mElement == self.specChar[aCharacter]:
                        eChar = (aCharacter - keyText) % 24 # number of special characters
                        string_output += self.specChar[eChar]

            elif (self.isNumber(mElement)):
                for aNumber in self.numersS:
                    if mElement == self.numersS[aNumber]:
                        aNum = (aNumber - keyText) % 10
                        string_output += self.numersS[aNum]

            elif (self.isCharacter(mElement)):
                for aLetter in self.alphabets:
                    if(mElement.lower() == self.alphabets[aLetter]):
                        eLetter = ((aLetter - keyText) % 26) # number of letters
                        string_output += self.alphabets[eLetter]

            else:
                string_output += mElement

        print(string_output)
        encryptedFile = open("orginalFile.txt", "w")
        encryptedFile.write(string_output)
        encryptedFile.close()



"""

test1 = caesarCipher()
#plainText = test1.readFileText('text.txt')
#test1.encrypt(plainText)

plainText2 = test1.readFileText('EncryptedFile.txt')
test1.decrypt(plainText2)
"""
