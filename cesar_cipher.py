def cesar_cipher(text, shift):
    # list to save new letters
    encoded_chars = []

    for char in text:
        if char.isupper():
            # logic to run the uppercase alphabet and not break it
            encoded_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encoded_chars.append(encoded_char)
        elif char.islower():
            # same thing here, but in lower case
            encoded_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encoded_chars.append(encoded_char)
        else:
           # if it's a space or a point, leave it alone and just ignore it
            encoded_chars.append(char)

   # put everything together and return the finished text
    return "".join(encoded_chars)

# running the code...
if __name__ == "__main__":
    # asks what the user wants to encrypt
    user_input = input("Enter the message to encrypt: ")
    try:
        # get the jump number (the key)
        shift_value = int(input("Enter the shift number (key): "))
        
        result = cesar_cipher(user_input, shift_value)

        print(f"\nOriginal: {user_input}")
        print(f"Encrypted: {result}")
    except ValueError:
       # if user types a letter where it should be a number
        print("Invalid input! Please enter a valid integer for the shift.")
