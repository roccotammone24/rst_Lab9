def encode(password):
    encoding = []
    output = ""
    for num in password:
        encoding.append(int(num))
    for num in encoding:
        num += 3
        output += str(num)
    return output


def decoder(password):
    decoding = []
    output = ""
    for num in password:
        decoding.append(int(num))
    for num in decoding:
        num -= 3
        output += str(num)
    return output


if __name__ == '__main__':
    while True:
        print("Menu")
        print("-------------")
        print("1.Encode")
        print("2.Decode")
        print("3.Exit")
        choice = input("Please enter an option: ")
        if choice == "1":
            password = input("Enter a password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored")
        if choice == "2":
            new_password = decoder(encoded)
            print("The encoded password is: ", encoded, " and the original password is: ", new_password)
        elif choice == "3":
            return False



