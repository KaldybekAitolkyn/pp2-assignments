txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(len(a))

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

a = "Hello"
b = "World"
c = a + b
print(c)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

txt = "Hello\tWorld!"
print(txt) 

txt = "Hello\rWorld!"
print(txt) 



a = "Hello, World! {}"
print(a.capitalize())
print(a.casefold())
print(a.center(20))
print(a.count("e"))
print(a.encode())
print(a.endswith("!"))
print(a.expandtabs(2))
print(a.find("e"))
print(a.format("John"))
print(a.index("e"))
print(a.isalnum())
print(a.isalpha())
print(a.isascii())
print(a.isdecimal())
print(a.isdigit())
print(a.isidentifier())
print(a.islower())
print(a.isnumeric())
print(a.isprintable())
print(a.isspace())
print(a.istitle())
print(a.isupper())
print(a.join("John"))
print(a.ljust(20))
print(a.lower())
print(a.lstrip())
print(a.maketrans("H", "J"))
print(a.partition("e"))
print(a.replace("e", "a"))
print(a.rfind("e"))
print(a.rindex("e"))
print(a.rjust(20))
print(a.rpartition("e"))
print(a.rsplit())
print(a.rstrip())
print(a.split())
print(a.splitlines())
print(a.startswith("H"))
print(a.strip())
print(a.swapcase())
print(a.title())
print(a.translate("H"))
print(a.upper())
print(a.zfill(5))