

uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

direction=input("type E or D: ").lower()
text=input("msg: ").upper()
shift=int(input("type shift no: "))

def caesar(original_txt,shift_amount,encode_decode):
    output_txt=''
    if encode_decode == 'd':  # already lowercase due to .lower()
        shift_amount *= -1

    for letter in original_txt:



        shifted_position=uppercase_letters.index(letter) + shift_amount
        shifted_position %= len(uppercase_letters)
        output_txt+= (uppercase_letters[shifted_position]).lower()


    print(f"here is your text: {output_txt}")

caesar(encode_decode=direction,original_txt=text,shift_amount=shift)