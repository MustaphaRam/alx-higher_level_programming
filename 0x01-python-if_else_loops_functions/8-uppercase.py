#!/usr/bin/python3
def uppercase(str):
    str2 =""
    for i in range(len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            str2 += chr(ord(str[i])-32)
        else:
            str2 += str[i]
    print("{}".format(str2))
