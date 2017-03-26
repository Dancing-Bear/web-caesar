def alphabet_position(letter):
    """Receives alphabetic character letter and returns its paired value"""

    alpha_nums = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alphabet)):
        alpha_nums[alphabet[i]] = i
        alpha_nums[alphabet[i].upper()] = i
    number = alpha_nums[letter]
    return number


def rotate_character(char, rot):
    """Receives character char and returns as is if non-alphabetic, otherwise
    finds and returns new letter according to rotation amount rot, using
    alphabet_position"""

    if char.isalpha() == False:
        return char

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    number = alphabet_position(char) + rot
    if number > 25:
        encrypted_number = number % 26
    else: encrypted_number = number

    for letter in alphabet:
        if alphabet_position(letter) == encrypted_number:
            encrypted_letter = letter
            if char == char.upper():
                encrypted_letter = encrypted_letter.upper()
                return encrypted_letter
            else:
                return encrypted_letter


def encrypt(text, rot):
    """Receives string text and creates and returns its encrypted form according
    to rotation amount rot, using rotate_character"""

    encrypted_text = ""
    for char in text:
        if char == " ":
            encrypted_text = encrypted_text + char
        else:
            encrypted_text = encrypted_text + rotate_character(char, rot)
    return encrypted_text
