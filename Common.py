

def hex2bytearray(hex):

  hex_chars = "0123456789abcdef"

  if len(hex)%2!=0:
    raise ValueError

  hex_pairs = [(hex[i], hex[i+1]) for i in range(0, len(hex), 2)]

  print("Hex pairs: {0}".format(hex_pairs))

  output = bytearray()
  for pair in hex_pairs:
    print("First: {0}, second: {1}, value: {2}".format(hex_chars.find(pair[0]), hex_chars.find(pair[1]), 16*hex_chars.find(pair[0]) + hex_chars.find(pair[1])))
    output += bytes([ 16*int(hex_chars.find(pair[0])) + hex_chars.find(pair[1]) ])

  return output

def bytearray2base64(barray):
  base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"