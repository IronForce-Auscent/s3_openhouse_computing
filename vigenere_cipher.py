class VingenereCipher:

  def __init__(self, case_sensitive: bool=False, alphabet: str="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    self.case_sensitive = case_sensitive
    self.ALPHABET = alphabet

  def _generate_key_string(self, text: str, key: str) -> str:
    """
    Checks if the key is of the same length as the text, if not, extend it
    """
    if len(text) > len(key):
      key = key * (len(text)//len(key)+1)
    return key

  def encrypt(self, text: str, key: str) -> str:
    """
    Encrypts the text by the given key
    """
    for k in key:
      k = k if self.case_sensitive else k.upper()
      if k not in self.ALPHABET:
        raise ValueError("All characters in key must be valid")
    key = self._generate_key_string(text, key)
    ciphertext = ""
    for m, k in zip(text, key):
      m, k = (m, k) if self.case_sensitive else (m.upper(), k.upper()) # I have never done this before but it works so
      if m not in self.ALPHABET:
        ciphertext += m
      else: # Formula is C[i] = (M[i]+K[i]) mod 26
        ciphertext += self.ALPHABET[
          (self.ALPHABET.index(m)+self.ALPHABET.index(k)) % len(self.ALPHABET)
        ]
    return ciphertext

  def decrypt(self, text: str, key: str) -> str:
    """
    Decrypts the text using the given key
    """
    for k in key:
      k = k if self.case_sensitive else k.upper()
      if k not in self.ALPHABET:
        raise ValueError("All characters in key must be valid")
    key = self._generate_key_string(text, key)
    ciphertext = ""
    for c, k in zip(text, key):
      c, k = (c, k) if self.case_sensitive else (c.upper(), k.upper()) # I have never done this before but it works so
      if c not in self.ALPHABET:
        ciphertext += c
      else: # Formula is M[i] = (C[i]-K[i]) mod 26
        ciphertext += self.ALPHABET[
          (self.ALPHABET.index(c)-self.ALPHABET.index(k)) % len(self.ALPHABET)
        ]
    return ciphertext