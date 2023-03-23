class VigenereCipher():
    """
    A class used to encrypt and decrypt a string (plaintext or ciphertext) using the Vigenere Cipher given 
    the key

    Attributes:
        - check_encrypt_key: 
    """
    def __init__(self):
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

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
        return new_key
    
    def generate_shifted_alphabet(self, key):
        """
        Generates a shifted alphabet for a Vigenere Cipher using the provided key.

        Parameters:
            key (str): The key used to generate the shifted alphabet.

        Returns:
            shifted_alphabet (list): A list containing the shifted alphabet for the Vigenere Cipher.
        """
        # Create a list to store the shifted alphabet
        shifted_alphabet = []

        # Iterate over each character in the key
        for i, char in enumerate(key):
            # Calculate the shift amount for the current character
            shift_amount = ord(char) - ord('a')

            # Generate the shifted alphabet for the current character
            shifted_letters = []
            for j in range(26):
                shifted_letters.append(chr((j + shift_amount) % 26 + ord('a')))

            # Add the shifted alphabet for the current character to the list
            shifted_alphabet.append(shifted_letters)

        return shifted_alphabet

    def encrypt(self, key, plaintext):
        key = self.check_encrypt_key(plaintext, key)
        plaintext = list(plaintext)
        ciphertext = ""
        shifted_alphabet = self.generate_shifted_alphabet(key)
        for i, char in enumerate(plaintext):
            shifted_alpha = shifted_alphabet[i]
            if char.islower():
                ciphertext += shifted_alpha[self.alphabet.index(char.upper())]
            elif char.isupper():
                ciphertext += shifted_alpha[self.alphabet.index(char)].upper()
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, key, ciphertext):
        # Generate the shifted alphabet for the key
        shifted_alphabet = self.generate_shifted_alphabet(key)

        # Initialize a list to store the plaintext
        plaintext = []

        # Iterate over each character in the ciphertext
        for i, char in enumerate(ciphertext):
            # If the character is not an uppercase letter, add it to the plaintext as-is
            if not char.isupper():
                plaintext.append(char)
            else:
                # Otherwise, calculate the index of the character in the shifted alphabet
                shift_amount = ord(key[i % len(key)]) - ord('a')
                shifted_index = (self.alphabet.index(char) - shift_amount) % 26

                # Add the corresponding plaintext character to the plaintext list
                plaintext.append(self.alphabet[shifted_index])

        # Join the plaintext list into a single string and return it
        return ''.join(plaintext)
