alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
key = ""
encrypted_alphabet = []

def generate_encrypted_alphabet(a_plain):
  """
  Generates a shifted version of the alphabet

  Status: Completed
  Remarks: Being rewritten to have better readability (seriously, what the hell was I smoking when I wrote this...)
  """
  global encryted_alphabet
  encrypted_alphabet = []
  a_index = lambda d: alphabet.index(d) if d.isalpha() else d
  for x in range(26):
    if not a_plain[x].isalpha():
      encrypted_alphabet.append(a_plain)
    elif (x + a_index(a_plain[x])) > 25:
      encrypted_alphabet.append(alphabet[(a_index(a_plain[x]) + x) - 26])
    else:
      encrypted_alphabet.append(alphabet[(a_index(a_plain[x]) + x)])
      # print(alphabet[(a_index + x)])
  print(encrypted_alphabet)
  return encrypted_alphabet


def check_key(plaintext, key):
  """
  Checks if the key is of the same length as the plaintext, and if it is not, extends the key such that its length is the same as the plaintext's

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


def encrypt(plaintext, key):
  """
  Encrypts the plaintext by the given key, and returns it. 

  Status: Completed
  Remarks: More testing with different types of plaintext and keys are required to ensure that the code works well
  """
  global alphabet
  plaintext_breakdown = [plaintext[i] for i in range(len(plaintext))]
  print(plaintext_breakdown)
  encrypted_string = ""
  encrypted_alphabet = []
  extended_key = check_key(plaintext, key)
  for x in range(len(plaintext)):
    encrypted_alphabet = generate_encrypted_alphabet(plaintext_breakdown[x].upper())
    print(encrypted_alphabet)
    if plaintext_breakdown[x].islower():
      encrypted_string += encrypted_alphabet[alphabet.index(extended_key[x].upper())].lower()
    elif plaintext_breakdown[x].isupper():
      encrypted_string += encrypted_alphabet[alphabet.index(extended_key[x].upper())].upper()
    else:
      encrypted_string += plaintext_breakdown[x]

  return encrypted_string

def decrypt(plaintext, key):
  """
  Decrypts a plaintext using the given key

  Status: Work in Progress
  Remarks: N/A (as of now)
  """