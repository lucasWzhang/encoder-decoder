def encode(file):
    with open('encrypted.txt', 'w') as new_file:
        with open (file, 'r') as original_file:
            for line in original_file:
                for char in line:
                    if char.isalpha():
                        if char.isupper():
                            number = ord(char) - ord('A')
                            number = (number + 3) % 26
                            char = chr(ord('A') + number)
                            new_file.write(char)
                        else:
                            number = ord(char) - ord('a')
                            number = (number + 3) % 26
                            char = chr(ord('a') + number)
                            new_file.write(char)

                    else:
                        new_file.write(char)
    return 'encrypted.txt'
        
def decode(file):
    with open('decrypted.txt', 'w') as new_file:
        with open(file, 'r') as original_file:
            for line in original_file:
                for char in line:
                    if char.isalpha():
                        if char.isupper():
                            number = ord(char) - ord('A')
                            number = (number - 3) % 26
                            char = chr(ord('A') + number)
                            new_file.write(char)
                        else:
                            number = ord(char) - ord('a')
                            number = (number - 3) % 26
                            char = chr(ord('a') + number)
                            new_file.write(char)

                    else:
                        new_file.write(char)
    return 'decrypted.txt'

print('This is the encoded file:\n')

encoded_file = encode('shapespear.txt')

with open(encoded_file) as file:
    print(file.read())

print('This is the decoded file: \n')

decoded_file = decode('encrypted.txt')

with open(decoded_file) as file:
    print(file.read())

