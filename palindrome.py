# This only works with three-digits numbers
what = input ("Enter a three-digit number: ")

a = int(what)%10


b = int(what)/10

c = int(b)%10
d = int(b/10)

if a == d:
    print("The number you entered is a palindrome")

else:
    print("The number you entered is not a palindrome")


