
while True:

    what = input("Enter a number or a word: ")
    
    if what[::1] == what[::-1]:
        print("The input you entered is a palindrome")
    else:
        print("The input you entered is not a palindrome")




