from library import  Librarian, Teacher

print('*' * 25)
librarian = Librarian.import_from_file('librarians.src')
[print(el) for el in librarian]

print('*' * 25)
teachers = Teacher.import_from_file('teachers.src')
[print(el) for el in teachers]


