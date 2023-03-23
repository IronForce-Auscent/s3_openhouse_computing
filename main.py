from vigenere_fixed import VigenereCipher

vigenere_cipher = VigenereCipher()
key, string = "test", "Your Mother"
ciphertext = vigenere_cipher.encrypt(key, string)
result = vigenere_cipher.decrypt(key, ciphertext)
print(ciphertext)
print(result)