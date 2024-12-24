# Домашнее задание по теме "Позиционирование в файле"


def custom_write(file_name, strings):
    strings_positions = {}

    # Открываем файл для записи в режиме 'w' с кодировкой utf-8
    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings, start=1):  # Начинаем с 1 для нумерации строк.
            start_position = file.tell()  # Получаем текущую позицию (в байтах) перед записью
            file.write(string + '\n')  # Записываем строку и добавляем перевод строки.
            strings_positions[(index, start_position)] = string  # Сохраняем в словарь

    return strings_positions


# Пример использования функции
if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)

