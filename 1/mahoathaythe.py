def substitution_cipher(text, substitution_map):
    encrypted_text = []
    for char in text:
        if char in substitution_map:
            encrypted_char = substitution_map[char]
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)  # Giữ nguyên ký tự nếu không có trong bản đồ thay thế
    return ''.join(encrypted_text)

# Ví dụ mã hóa với bản đồ thay thế đơn giản
plaintext = "Hello World!"
simple_substitution_map = {
    'H': 'X',
    'e': 'Y',
    'l': 'Z',
    'o': 'A',
    'W': 'B',
    'r': 'C',
    'd': 'D',
    '!': 'E'
}
ciphertext = substitution_cipher(plaintext, simple_substitution_map)
print("Ciphertext:", ciphertext)
