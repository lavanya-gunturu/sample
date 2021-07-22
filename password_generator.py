import string
import random

#define the uppercase alphabets
StrUpperCase = string.ascii_uppercase

#define the lowercase alphabets
StrLowerCase = string.ascii_lowercase

#define the numbers or digits
Numb = string.digits

#define the special characters
Char = string.punctuation

pwdlen = int(input("Enter the password length\n"))
s=[]
s.extend(list(StrUpperCase))
s.extend(list(StrLowerCase))
s.extend(list(Numb))
s.extend(list(Char))

print("Your random password is: ")
print("".join(random.sample(s,pwdlen)))