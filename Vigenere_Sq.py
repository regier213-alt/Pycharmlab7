def vigenere_header(alphabet):
    alpha_len = len(alphabet)
    print('|  ', end=' ')
    for i in range(alpha_len):
        print(f"| {alphabet[i]}", end=' ')
    print('|')
    print(f"{'|---'*(alpha_len + 1)}|")

def vigenere_sq(alphabet):
    alpha_len = len(alphabet)
    vigenere_header(alphabet)
    for shift in range(alpha_len):
        for i in range(alpha_len):
            if i == 0:
                c = alphabet[(i + shift) % alpha_len]
                print(f"|{c} ", end=' ')
                print(f"|{c} ", end=' ')
            else:
                print(f"| {alphabet[(i + shift) % alpha_len]}", end=' ')
        print('|')

def letter_to_index(letter, alphabet:str):
    return alphabet.lower().index(letter.lower())

def index_to_letter(index, alphabet):
    if 0 <= index < len(alphabet):
        return alphabet[index]
    return''

def vigenere_index(key_letter, plaintext_letter, alphabet):
    return (letter_to_index(key_letter, alphabet) +
            letter_to_index(plaintext_letter, alphabet)) % len(alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = ''
    counter = 0
    for c in plaintext:
        if c == ' ':
            cipher_text += ' '
            pass
        elif(c.upper() in alphabet):
            cipher_text += index_to_letter(vigenere_index(key[counter % len(key)], c, alphabet), alphabet)
            counter += 1
    return cipher_text

def undo_vigenere_index(key_letter, cypher_letter, alphabet):
    key_index = alphabet.index(key_letter)
    cypher_index = alphabet.index(cypher_letter)

    plain_index = (cypher_index - key_index) % len(alphabet)

    return alphabet[plain_index]

def decrypt_vigenere(key, cipher_text, alphabet):
    plain_text = ''
    for i in range(len(cipher_text)):
        key_letter = key[i % len(key)]
        cipher_letter = cipher_text[i]
        plain_letter = undo_vigenere_index(
            key_letter, cipher_letter, alphabet
        )
        plain_text += plain_letter
    return plain_text



key = 'BANANABRD'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = 'Up He Sees Me Im Down'
#vigenere_sq(alphabet)
#print(letter_to_index('H', alphabet))
#print(index_to_letter(7, alphabet))
#print(
#   index_to_letter(
#        vigenere_index('B', 'H', alphabet),alphabet)
#   )

#print(encrypt_vigenere(key, message, alphabet))

#print(undo_vigenere_index('B', 'I', alphabet))
print(decrypt_vigenere('B', 'I', alphabet))