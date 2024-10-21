def serialize(data: list[dict[str, int | str]], path: str):
    """
        Функция сериализации(сохранения) данных в файл

        Аргументы:
        data - список, состоящий из словарей, каждый из
        которых представляет отдельную запись. Ключи словаря - строки,
        а значения - строки или целые числа
        path - путь до файла, в который нужно записать данные
"""
    with open(path, 'w', encoding='utf-8') as file:
        for record in data:
            line = ', '.join(f"{key}: {value}" for key, value in record.items())
            file.write(line + ';\n')


def deserialize(path: str) -> list[dict[str, int | str]]:
    """
        Функция десериализации(загрузки) данных из файла

        Аргументы:
        path - путь до файла, из которого нужно считать данные

        Возвращает список, аналогичный списку из функции `serialize`
    """
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    data = []
    for line in lines:
        line = line.strip().rstrip(';')
        if line:
            record = {}
            pairs = line.split(', ')
            for pair in pairs:
                key, value = pair.split(': ')
                if value.isdigit():
                    value = int(value)
                else:
                    value = value.strip('"')
                record[key] = value
            data.append(record)
    
    return data