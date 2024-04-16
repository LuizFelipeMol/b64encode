import base64

def main():
    while True:
        user_choice = input('Choose between encode, decode or quit to stop the program: ').lower()
        if user_choice == 'encode':
            text_encode = input('enter de text to encode: ').lower()
            text_encoded = base64.b64encode(text_encode.encode())
            print(text_encoded)
            break



        elif user_choice == 'decode':
            text_decode = input('Enter encoded text: ')
            text_decoded = base64.b64decode(text_decode,None, False)
            print(text_decoded)
            break

        elif user_choice == 'quit':
            break


        else:
            print('invalid')

if __name__ == "__main__":
    main()