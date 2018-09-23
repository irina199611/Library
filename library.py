class Library:
    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic

    def __str__(self):
            return f'библиотека:{self.name} {self.characteristic}.'

    @classmethod
    def import_from_file(cls, library):
        items_source = open(library, 'r', encoding='utf-8').readlines()
        items_source = list(map(lambda x: x.replace('\n', '').split(', '), items_source))
        items_schema = items_source.pop(0)
        items_source_as_dict = list(map(lambda x: dict(zip(items_schema, x)), items_source))
        items = []
        for item_dict in items_source_as_dict:
            _item = cls(**item_dict)
            items.append(_item)
        return items


class Librarian(Library):
    def __init__(self, name, author, book):
        self.name = name
        self.author = author
        self.book = book

    def __str__(self):
            return f'библиотекарь({self.name}): {self.author} {self.book}.'


class Teacher(Library):
    def __init__(self, name, date_birth, author, book):
        self.name = name
        self.date_birth = date_birth
        self.author = author
        self.book = book

    def __str__(self):
            return f' учитель({self.name}): {self.date_birth} {self.author} {self.book}.'

