#!/usr/bin/python3.9
# coding=utf-8

# Task 4

def encrypt(input_text):
    for ch in input_text:
        if ch.lower() == 'a' or ch.lower() == 'b' or ch.lower() == 'c':
            print(chr(ord(ch) + 23), end='')
        elif ch.isalpha():
            print(chr(ord(ch) - 3), end='')
        else:
            print(ch, end='')

if __name__ == "__main__":
    input_text = input('Plaintext: ')
    print(f"Caesar cipher: ", end='')
    encrypt(input_text)
    print()
