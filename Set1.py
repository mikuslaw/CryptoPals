import Common

def challenge_1():
  hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
  base64_string = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

  base64_encoded = Common.hex2bytearray(hex_string)

  print("Hex: {0}\nBase64: {1}\nExpected: {2}".format(hex_string, base64_encoded, base64_string))


if __name__ == "__main__":
  challenge_1()
