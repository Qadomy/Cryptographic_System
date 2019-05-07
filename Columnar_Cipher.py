

class columnar_cipher():

    def read_file(self, TextFile):
        file_text = open(TextFile, 'r')
        plain_text = file_text.read()
        file_text.close()

        return plain_text


    def encrypt(self, text):
        key_file = open('keyFile.txt', 'r')
        key = key_file.read()
        key_file.close()

        string_output = []
        seenLetter = None

        """clean the text by remove the whitespace and spaces"""
        text = text.strip().replace(' ', '')

        """knowing the length of the key and divided the length of text to length of keys
        to re-sorted the new text"""
        lengthC = (len(text) / len(key))

        """after we sort the text in new text we see if there is a additional spaces
        IF there a additional spaces we add the last character of text to last space"""

        from math import ceil
        text += text[-1] * int(float("%.1f" % ((ceil(lengthC) - lengthC) * len(key))))

        """we sort the text in number of keys groups"""
        sectionV = [text[i::len(key)] for i in range(len(key))]

        for letter in sorted(key): # sorted: for give a numbers began 0 until the length of key
            if letter == seenLetter: # seenLetter: mean if the key have NONE
                index = key.find(letter, index + 1)
            else:
                index = key.find(letter)

            seenLetter = letter

            string_output.append(sectionV[index]) # so we add the first section of letters and so on


        """for connect the output groups of new text together without separate groups"""
        string_output = ''.join(string_output)
        print(string_output)


        """use pickle.dump for saved the text in .enc file type"""
        import pickle
        pickle.dump(string_output, open("EncryptedFileColummar.enc", 'wb'))

        """here for saved encypted text in txt file type to return decrypt"""
        encryptedFile = open("EncryptedFileColummar.txt", "w")
        encryptedFile.write(string_output)
        encryptedFile.close()



    def decrypt(self, text):
        key_file = open('keyFile.txt', 'r')
        key = key_file.read()
        key_file.close()


        string_output = []
        seenLetter = []

        lengthC = int(len(text) / len(key))
        """for re-sort the encrypt text to groups"""
        sectionsV = [text[i:i + lengthC] for i in range(0, len(text), lengthC)]

        for letter in key:
            index = ''.join(sorted(key)).find(letter) # here for sort the length of key
            while index in seenLetter:
                index += 1

            """[1]
               [1, 0]
               and so on"""
            seenLetter.append(index)
            string_output.append(sectionsV[index]) #['mnmqdm', 'yaeaoy']

            stringOrd = ''.join(string_output) # connect the separate groups together without spaces

            """we restore the the orignal text but in separate groups
                    ['my', 'na', 'me', 'qa', 'do', 'my']"""
            result = [stringOrd[i::lengthC] for i in range(lengthC)]

            orignalText = ''.join(result)
            print(orignalText)

            encryptedFile = open("orginalFileColummar.txt", "w")
            encryptedFile.write(orignalText)
            encryptedFile.close()




"""
test = columnar_cipher()
plain_text = test.read_file('text.txt')
test.encrypt(plain_text)

orignal_text = test.read_file('EncryptedFileColummar.txt')
test.decrypt(orignal_text)
"""