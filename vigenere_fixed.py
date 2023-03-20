class VigenereCipher():
    def __init__(self):
        self.lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.key = ""
    
    def check_encrypt_key(self, plaintext, key):
        """
        Checks if the key is of the same length as the plaintext, and if it is not, extends the key such that its length is the same as the plaintext

        Attributes:
        - plaintext: The original plaintext being used
        - key: The key that is being used to encrypt the plaintext

        Status: Completed
        Remarks: N/A (as of now)
        """
        new_key = ""
        k_index = 0
        while len(plaintext) > len(new_key):
            if (k_index + 1) == len(key):
                new_key += key[k_index]
                k_index = 0
            else:
                new_key += key[k_index]
                k_index += 1
        print(new_key)
        return new_key
    
    def generate_encrypted_alphabet(self, key):
        encrypted_alphabets = []
        letters = 