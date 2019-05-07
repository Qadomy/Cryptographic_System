
class vigenereCipher():

    def msg_and_key(self, textFile, keyFile):
        fileText = open(textFile, 'r')
        msg = fileText.read().upper()

        fileKey = open(keyFile, 'r')
        key = fileKey.read().upper()

        # we create variable to store mapped key
        key_map = ""

        j = 0
        for i in range(len(msg)):
            if(ord(msg[i]) == 32):  # 32 in ASCI code mean the space and here we ignoring it
                key_map += " "
            else:
                if j < len(key):
                    key_map += key[j]
                    j += 1
                else:
                    j = 0
                    key_map += key[j]
                    j += 1

        #print(key_map)     """QADOM YQA DOMYQAD OM YQADOM YQADOM YQA"""
        return msg, key_map

    """make a table of alphabets"""
    def create_vigenere_table(self):
        table = []
        for i in range(26):
            table.append([])

        for row in range(26):
            for column in range(26):
                if (row + 65) + column > 90: # here for moving back to A after Z
                    """after first row, 
                    each row will shift left one position compared the row above it"""
                    table[row].append(chr((row + 65) + column - 26))
                else:
                    table[row].append(chr((row + 65) + column))

        """here for printing the table 
                for row in table:
            for column in row:
                print(column, end=" ")
            print(end='\ n')"""

        return table

    def itr_count(self, mapped_key, message):
        counter = 0
        result = ""
        """starting alphabets from mapped key letter
        and finishing all 26 letters from it,

        from z we move to a"""

        for i in range(26):
            if mapped_key + i > 90:
                result += chr(mapped_key + (i - 26))
            else:
                result += chr(mapped_key + i)

        """counting the number of iterations"""
        for i in range(len(result)):
            if result[i] == chr(message):
                break
            else:
                counter += 1

        return counter


    """********************************************************************************"""

    """Function cipher_encryption for make encryption for the text"""
    def cipher_encryption(self, message, mapped_key):
        table = self.create_vigenere_table()
        encrypted_text = ""

        for i in range(len(message)):
            if(message[i] == chr(32)): # ignoring space
                encrypted_text += " "
            else:
                """getting the elemnts to specific index of table"""
                row = ord(message[i]) - 65
                column = ord(mapped_key[i]) - 65
                encrypted_text += table[row][column]
                print(table)


        print("Encrypted Message: {}".format(encrypted_text))
        self.saveEncryptedText(encrypted_text) # here we send the encrypted_text to save in new file
        import pickle
        pickle.dump(encrypted_text, open('EncryptedVignere.enc', 'wb'))

    """Function cipher_decryption for make decryption for the text"""
    def cipher_decryption(self, message, mapped_key):
        table = self.create_vigenere_table()
        decrypt_text = ""

        for i in range(len(message)):
            if(message[i] == chr(32)): # here for space to ignoring
                decrypt_text += " "
            else:
                """here for add the number of iteration"""
                decrypt_text += chr(65 + self.itr_count(ord(mapped_key[i]), ord(message[i])))

        print("Decrypted Message: {}".format(decrypt_text))
        self.saveDecryptedText(decrypt_text)

    """********************************************************************************"""


    """Function for save the new encrypted text in 'EncryptedVignere.txt' file"""
    def saveEncryptedText(self, encrypted_text):
        encryptedFile = open("EncryptedVignere.txt", 'w')
        encryptedFile.write(encrypted_text)
        encryptedFile.close()

    """Function for save the file decrypted text (return to orignal text)"""
    def saveDecryptedText(self, decrypted_text):
        decryptedFile = open('OrignalVignere.txt', 'w')
        decryptedFile.write(decrypted_text)
        decryptedFile.close()



    """********************************************************************************"""
    """********************************************************************************"""
    def main(self, message, mapped_key):
        print("The Key and text just in alphabets")
        choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2):"))

        if choice == 1:
            print("---Encryption---")
            message, mapped_key = self.msg_and_key(message, mapped_key)
            self.cipher_encryption(message, mapped_key)


        elif choice == 2:
            print("---Decryption---")
            message, mapped_key = self.msg_and_key(message, mapped_key)
            self.cipher_decryption(message, mapped_key)

        else:
            print("Wrong Choice!!")





tst = vigenereCipher()
tst.main('text.txt', 'vignereKey.txt')
"""
test = vigenereCipher()
#test.main('text.txt', 'vignereKey.txt')
#test.main('EncryptedVignere.txt', 'vignereKey.txt')
message, mapped_key = test.msg_and_key('text.txt', 'vignereKey.txt')

test.cipher_encryption(message, mapped_key)
"""