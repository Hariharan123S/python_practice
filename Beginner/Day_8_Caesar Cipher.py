import art

print(art.logo)
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w",
            "x", "y", "z"]


def caesar(original_text, shift_amount, encode_or_decode):
    cort_list = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letters in original_text:
        shifted = alphabet.index(letters) + shift_amount
        shifted %= len(alphabet)
        cort_list += alphabet[shifted]
        if letters not in original_text:
            cort_list += letters

    print(f"Here is the {direction}d result: " + cort_list)


case = True
while case:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("Type 'yes' for if you want to do again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        case = False
        print("Bye!Bye!")
