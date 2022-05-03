#In Class Demo
#encrypt letters such that capital Z shifted 1 is capital A and lowercase z shifted 1 is lowercase a
def encrypt(text,s):
  a_result = ""
  for i in range(len(text)):
    char = text[i]
  # traverse the plain text
    if(char.isupper()):
    # Encrypt uppercase characters in plain text
    # convert letter into unicode
    # make A unicode 0 by subtracting 65
    # add shift
    # allow wraparound by mod 26
    # make A's unicode 65 again by adding 65
    # convert unicode to letter
      e_result += chr((ord(char) - 65 + s) % 26 + 65)
    else:
    # Async Work: Encrypt lowercase characters in plain text
      #result += "replace me with code"
      a_result += chr((ord(char) - 97 + s) % 26 + 97) 
  return result

  #enter alphabetic text without spaces and a desired shift
#text = "ABab"
text = "Eric"
s = 27

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Encrypted Text: " + encrypt(text,s))

#Homework Bell Pepper Version: Write a function that decrypts a symmetric cipher with a given shift
#text = "DCdc"
text = encrypt(text, s)
#s = 29

def decrypt(text,s):
  a_result = ""
  for i in range(len(text)):
    char = text[i]
    if(char.isupper()):
      a_result += chr((ord(char) - 65 - s) % 26 + 65)     
    else:
      a_result += chr((ord(char) - 97 - s) % 26 + 97)
  return a_result

print("Encrypted Text : " + text)
print("Shift pattern : " + str(s))
print("Decrypted Text: " + decrypt(text,s))
