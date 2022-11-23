def encrypt(message, key):
  temp_char = 0
  encrypted = ""
  message_chars = [message[i] for i in range(len(message))]
  for char in message_chars:
    if char.islower():
      temp_char = ord(char) + key
      while temp_char > 122:
        temp_char = temp_char - 122 + 96

      encrypted += chr(temp_char)
    elif char.isupper():
      temp_char = ord(char) + key
      while temp_char > 90:
        temp_char = temp_char - 90 + 64
      encrypted += chr(temp_char)
    else:
      encrypted += char

  return encrypted

def decrypt(message, key):
  temp_char = 0
  decrypted = ""
  message_chars = [message[i] for i in range(len(message))]
  for char in message_chars:
    if char.islower():
      temp_char = ord(char) - key
      while temp_char < 97:
        temp_char = 122 - (97 - temp_char)
      decrypted += chr(temp_char)
    elif char.isupper():
      temp_char = ord(char) - key
      while temp_char < 65:
        temp_char = 90 - (65 - temp_char)
      decrypted += chr(temp_char)
    else:
      decrypted += char

  return decrypted

def main():
  mode = input("Please enter 'E' to encrypt or 'D' to decrypt: ")
  message = input("Please enter the message or ciphertext: ")
  key = input("Please enter number of positions: ")
  #while int(key) < 0 or not key.isnumeric():
   # key = input("Please enter number of positions: ")

  if mode.lower() == 'e':
    print(encrypt(message, int(key)))
  elif mode.lower() == 'd':
    print(decrypt(message, int(key)))
  else:
    print("Invalid mode selected")


"""
To run the code:

import INTERFACE

INTERFACE.main()
"""