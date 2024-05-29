def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return "".join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_encrypt(plain_text, key):
    cipher_text = []
    key = generate_key(plain_text, key)
    for i in range(len(plain_text)):
        x = (ord(plain_text[i]) + ord(key[i]) - 2 * ord('A')) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text)

def vigenere_decrypt(cipher_text, key):
    orig_text = []
    key = generate_key(cipher_text, key)
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return "".join(orig_text)

# Example usage:
if __name__ == "__main__":
    text = "HELLO"
    keyword = "KEY"
    
    encrypted_text = vigenere_encrypt(text, keyword)
    print(f"Encrypted Text: {encrypted_text}")

    decrypted_text = vigenere_decrypt(encrypted_text, keyword)
    print(f"Decrypted Text: {decrypted_text}")
