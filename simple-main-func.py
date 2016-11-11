#!/usr/bin/python

def number():
    num = []
    for i in range(5):
        num.append(i + 1)
        
    return num

def main():
    listNum = number()
    print(listNum)


main()

