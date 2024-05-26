def to_uppercase(text):
    """Функция делающая все слова капсом"""
    return text.upper()

#input_string = "Привет, мир!"
#result = to_uppercase(input_string)
#print(result)

def make_title_case(input_string):
    """Функция, делающая все первый буквы слов заглавными"""
    return ' '.join(word.capitalize() for word in input_string.split())

# Пример использования
#input_string = "пример строки, которую нужно преобразовать"
#output_string = make_title_case(input_string)
#print(output_string)