'''
Цикл while. Проверка имени.
'''
# Цикл - разновидность управляющей конструкции в высокоуровневых языках программирования,
# предназначенная для организации многократного исполнения набора инструкций.

name = input('Кто создатель Python? Ваш ответ: ')
while name != 'Guido':
    print('НЕ Верно!')
    name = input('Кто создатель Python? Ваш ответ: ')
print('Совершенно верно!')