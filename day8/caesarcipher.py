#user enters msg
#hi
#user enters shift
#2




#decoding

uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#print(uppercase_letters)

def encoding_method(msg,shift_no):
    encoded_list = []
    for letter in msg:
        if letter in uppercase_letters:
            new_idx=uppercase_letters.index(letter)+shift_no
            new_idx=new_idx % len(uppercase_letters)
            encoded_list+=(uppercase_letters[new_idx])
        else:
            encoded_list.append(letter)
    encoded_msg= (''.join(encoded_list))
    return encoded_msg

def decoding_method(msg,shift_no):
    decoded_list = []
    for letter in msg:
        #print(letter)
            new_idx=uppercase_letters.index(letter)-shift_no
            new_idx = new_idx % len(uppercase_letters)   #this makes sure index out of range is handled
            decoded_list+=(uppercase_letters[new_idx])
            if letter not in uppercase_letters:
                decoded_list.append(letter)
    decoded_msg=(''.join(decoded_list))
    return  decoded_msg

def caesar_cipher():
    continue_coding=True
    while continue_coding:
        print('******************************************************************************')
        user_choice=input("Please enter E for encoding the msg\n D for decoding the msg\n N to exit\n enter here: ").upper()


        if user_choice=='E':
            msg = input("message: ").upper()
            shift_no = int(input("shift no"))
            enc_msg = encoding_method(msg, shift_no)
            print(f"your encoded msg: {enc_msg}")
        elif user_choice=='D':
            msg = input("message: ").upper()
            shift_no = int(input("shift no"))
            dec_msg = decoding_method(msg, shift_no)
            print(f"your decoded msg: {dec_msg}")

        elif user_choice=='N':
            continue_coding=False
            print("Thanks for using caesar cipher. Bye!")
        else:
            print("please select E/D/N only")



#print(''.join(encoded_list))
#print(''.join(decoded_list))

caesar_cipher()

