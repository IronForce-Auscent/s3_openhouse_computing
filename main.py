from vigenere_fixed import VigenereCipher
vigenere_cipher = VigenereCipher()
print(vigenere_cipher.generate_encrypted_alphabet('Hello World'))

"""import vigenere_cipher

sample_plain = "Hello World"
sample_key = "Test"
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print(alphabet)
print(vigenere_cipher.encrypt(sample_plain, sample_key))

for i in range(len(sample_plain)):
  print(vigenere_cipher.generate_encrypted_alphabet(sample_plain[i].upper()))
"""