import re

ROMAN_NUMERAL_PATTERN =\
    r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

regex = re.compile(ROMAN_NUMERAL_PATTERN)

def is_roman_numeral(number: str) -> bool:
    return regex.match(number)

def main():
    try:
        user_input = input("Введите число римскими цифрами: ")
        if is_roman_numeral(user_input):
            print("Это валидное римское число")
        else:
            print("Это не валидное римское число")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
