#!/usr/bin/python3
def uppercase(str):
    for char in str:
        charAsciiValue = ord(char)
        if ord(char) >= 97 and ord(char) <= 122:
            charAsciiValue -= 32
        print(chr(charAsciiValue), end="")
    print()
