def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")
    cipher_text = ''
    for char in text:
        if char.isalpha():
            char = char.upper()
            x = ord(char) - ord('A')
            encrypted_char = (a * x + b) % 26 + ord('A')
            cipher_text += chr(encrypted_char)
        else:
            cipher_text += char
    return cipher_text

def affine_decrypt(cipher_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")
    plain_text = ''
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("Multiplicative inverse of 'a' modulo 26 does not exist.")
    for char in cipher_text:
        if char.isalpha():
            char = char.upper()
            y = ord(char) - ord('A')
            decrypted_char = (a_inv * (y - b) % 26) + ord('A')
            plain_text += chr(decrypted_char)
        else:
            plain_text += char
    return plain_text

# Example usage:
if __name__ == "__main__":
    text = "HELLO WORLD"
    a = 5  # Key 'a' must be coprime with 26
    b = 8  # Key 'b' can be any integer

    encrypted_text = affine_encrypt(text, a, b)
    print(f"Encrypted Text: {encrypted_text}")

    decrypted_text = affine_decrypt(encrypted_text, a, b)
    print(f"Decrypted Text: {decrypted_text}")
