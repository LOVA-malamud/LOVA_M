
# call function from outside
# int(  input('number?')  )

name = 'danny' # str = input('whats your name? ')

print(name, 'your name is in length', len(name))

#       variable name
print(f"{name} your name is in length len(name)")

#     text-name
print(f"name your name is in length len(name)")

print(name, 'your name is in length', len(name))
print(f"{name} your length name is in {len(name)}")

first_name = "Petros"
last_name = "Borchardt"
id = "63 251283 B 185"
phone = "0419-0288803"

print(first_name, last_name, "id number ", id, " phone ", phone)
# last_name  first_name   id                          phone
# Borchardt, Petros id[3 251283 B 185] phone-number(0419-0288803)

# outer execution
# print(int( input('number?') ))
print(str.upper( first_name ))

# inner execution
print(first_name.upper())

################# number of chcaracters
text: str = "Hello, World!!"
print(len("Hello, World!!"))
print(len(text))

################# remove spaces from start + end
text1: str = "   Hello, World!!   "
print(text.strip())

################# lower-case of all characters
text2: str = "Hello, World!!"
print(text2.lower())

################# upper-case all characters
text3: str = "Hello, World!!"
print(text3.upper())

################# switch between text old -> new
text4: str = "Hello, World!!"
print(text4.replace("World", "Python"))
print(text4.replace("l", "t"))
print(text4.replace("t", ""))

################# make list of words with specific seperator
text5: str = "Hello, World!! good morning"
print(text5.split())  # same as ' '
text5 = "Hello,*World!!*good*morning"
print(text5.split('*'))

################# upper -> lower, lower -> upper
print(f'{"AasdasBcccC".swapcase()}', "AasdasBcccC".swapcase().swapcase())

text6: str = "Hello, World!! good morning"
print('text6.startswith("Hello") ?', text6.startswith("Hello"))

text7: str = "Hello, World!! good morning"
print('text7.endswith("good morning") ?', text7.endswith("good morning"))

############ make the first letter upper case, all other lwoer case
text8: str = "hello, world!! Good morning"
print('text8.capitalize() ', text8.capitalize())

############ each new word starts with upper case, all other lower case
text9: str = "hello, world!! good morNing"
print('text9.title() ', text9.title())



print('"1234" text10.isalpha() ', "1234".isalpha())
print('"abcd".isalpha()', "abcd".isalpha())
print('"abcd_".isalpha()', "abcd_".isalpha())
print('"abcd*".isalpha()', "abcd1*".isalpha())

print('"1234" text10.isdigit()', "1234".isdigit())
print('"abcd".isdigit()" ', "abcd".isdigit())
print('"abcd1".isdigit()" ', "abcd1".isdigit())

print('"Aab".islower()', "Aab".islower())
print('"aab".islower()', "aab".islower())
print('"Aab".isupper()', "Aab".isupper())
print('"ABC".isupper()', "ABC".isupper())

print('"AasdasBcccC".swapcase()', "AasdasBcccC".swapcase())

print('"42".zfill(5)', "42".zfill(5))

print('Hello!'.center(12, '-'))
print('Hello!'.center(12, ' '))

print('"     ".isspace()', "    ".isspace())

print("Hello python course")
print('   [0]', "Hello python course"[0])
print("  [-1]", "Hello python course"[-1])
print("[::-1]", "Hello python course"[::-1])
print("  [5:]", "Hello python course"[5:])
print("  [:8]", "Hello python course"[:8])
print(" [::2]", "Hello python course"[::2])

while True:
    input_year = input('year?')
    if input_year.isdigit():
        break
year_birth: int = int(input_year)