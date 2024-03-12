
def show_contacts(): # Показать все контакты в справочнике
    with open('Phonebook.txt', 'r', encoding='UTF-8') as file:
        data = file.read()
    print(data)

def add_contact(text): # Добавить контакт в справочник
    with open('Phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write('\n'+text)


print('Основное меню:')
print(
    ' 1. Открыть справочник\n 2. Сохранить изменения\n 3. Показать контакты\n '
    '4. Добавить контакт\n 5. Найти контакт\n 6. Изменить контакт\n 7. Удалить контакт\n 8. Выход\n')

menu = ['1. Открыть файл', '2. Сохранить файл', '3. Показать контакты в справочнике', '4. Добавить контакт',
    '5. Найти контакт', '6. Изменить контакт', '7. Удалить контакт', '8. Выход']

choice = int(input('Какой пункт выбираем (укажите номер)?: '))

if choice == 3:
    print(f'Вы выбрали пункт: \n  {menu[choice-1]}:')
    show_contacts()
if choice == 4:
    print(f'Вы выбрали пункт: \n  {menu[choice - 1]}:')
    text = input('Введите запись: ')
    add_contact(text)
    print('Запись добавлена')









