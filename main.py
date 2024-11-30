import re
import requests

ROMAN_NUMERAL_PATTERN =\
    r"(?<!\w)\bM{0,3}(?:CM|CD|D?C{0,3})(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3})\b(?!\w)"
SITE = "https://www.britannica.com/topic/Roman-numeral"
FILENAME = "text.txt"
regex = re.compile(ROMAN_NUMERAL_PATTERN)


class HTTPError(Exception):
    def __init__(self, status_code: int, reason: str):
        self.status_code = status_code
        self.reason = reason

    def __str__(self):
        return f"request error:\
            \ncode {self.status_code}\
            \nreason: {self.reason}"


def is_roman_numeral(number: str) -> bool:
    return regex.match(number)

def get_roman_numerals_from_url(url: str) -> list:
    request = requests.get(url)
    if request.status_code != 200:
        raise HTTPError(request.status_code, request.reason)
    return regex.findall(request.text)

def get_roman_numerals_from_file(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as file:
        return regex.findall(file.read())

def main():
    try:
        matched_list_url = get_roman_numerals_from_url(SITE)
        matched_list_file = get_roman_numerals_from_file(FILENAME)

        print("Чтение валидных римских чисел с сайта:")
        for i in matched_list_url:
            print(i)
        
        print("Чтение валидных римских чисел с файла:")
        for i in matched_list_file:
            print(i)

        user_input = input("Введите число римскими цифрами: ")
        if is_roman_numeral(user_input):
            print("Это валидное римское число")
        else:
            print("Это не валидное римское число")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
