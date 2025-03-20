def main():
    # ------------------------------
    # Validation Methods
    # ------------------------------
    print("=== Validation Methods ===")
    # .isalpha() – checks if all characters are letters
    print("hello".isalpha())          # True
    print("hello123".isalpha())       # False

    # .isdigit() – checks if all characters are digits
    print("123".isdigit())            # True
    print("3.5".isdigit())            # False (because of the decimal point)

    # .isalnum() – checks if all characters are alphanumeric (letters and numbers)
    print("hello123".isalnum())       # True
    print("hello 123".isalnum())      # False (space is not alphanumeric)

    # .isspace() – checks if all characters are whitespace
    print("   ".isspace())            # True

    # .islower() – checks if all cased characters are lowercase
    print("hello".islower())          # True

    # .isupper() – checks if all cased characters are uppercase
    print("HELLO".isupper())          # True

    # .istitle() – checks if the string is title cased (each word starts with an uppercase letter)
    print("Hello World".istitle())    # True

    # .isnumeric() – checks if all characters are numeric (including Unicode numbers)
    print("123".isnumeric())          # True

    # .isdecimal() – checks if all characters are decimals (0-9)
    print("123".isdecimal())          # True

    # .isidentifier() – checks if the string is a valid Python identifier
    print("my_variable".isidentifier())  # True

    # .isascii() – checks if all characters are ASCII characters (0-127)
    print("hello".isascii())          # True
    print("héllo".isascii())          # False (because of the accented é)

    # ------------------------------
    # Utility Methods
    # ------------------------------
    print("\n=== Utility Methods ===")
    s = "   Hello World!   "
    print("Original string:", repr(s))
    
    # .strip(), .lstrip(), and .rstrip() – remove whitespace from both ends, left, or right
    print("strip():", repr(s.strip()))       # "Hello World!"
    print("lstrip():", repr(s.lstrip()))       # "Hello World!   "
    print("rstrip():", repr(s.rstrip()))       # "   Hello World!"

    # .upper() – converts to uppercase
    print("upper():", s.upper())               # "   HELLO WORLD!   "

    # .lower() – converts to lowercase
    print("lower():", s.lower())               # "   hello world!   "

    # .capitalize() – capitalizes the first character, lowercases the rest
    print("capitalize():", s.capitalize())     # "   hello world!   " (note: leading spaces remain)

    # .title() – converts to title case (each word starts with an uppercase letter)
    print("title():", s.title())               # "   Hello World!   "

    # .split() – splits the string into a list (default separator: any whitespace)
    print("split():", s.split())               # ['Hello', 'World!']

    # .join() – joins elements of an iterable into a string using the string as a separator
    words = ["Hello", "World!"]
    print("join():", " ".join(words))          # "Hello World!"

    # .replace() – replaces occurrences of a substring with another substring
    print("replace():", s.replace("World", "Python"))  # "   Hello Python!   "

    # .find() – returns the lowest index where a substring is found, or -1 if not found
    print("find('World'):", s.find("World"))   # 9

    # .count() – returns the number of occurrences of a substring
    print("count('l'):", s.count("l"))           # count of 'l' (case-sensitive)

    # .startswith() and .endswith() – checks if the string starts or ends with a given substring
    print("startswith('   Hello'):", s.startswith("   Hello"))  # True
    print("endswith('!   '):", s.endswith("!   "))                # True

if __name__ == "__main__":
    main()
