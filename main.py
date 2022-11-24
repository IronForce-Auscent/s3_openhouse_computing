import vigenere_cipher

sample_plain = "Hello World"
sample_key = "Test"

print(vigenere_cipher.VingenereCipher().encrypt(sample_plain, sample_key))
"""
for i in range(len(sample_plain)):
  print(vigenere_cipher.generate_encrypted_alphabet(sample_plain[i].upper()))
"""