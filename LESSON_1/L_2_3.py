# Логические операторы.

ale = 71    # Средняя продолжительность жизни.
age = int(input('Введите ваш возраст: '))

print('Ваш возраст равен средней продолжительности жизни', ale == age)
print('Ваш возраст НЕ равен средней продолжительности жизни', ale != age)
print('Ваш возраст меньше средней продолжительности жизни', age < ale)
print('Ваш возраст больше средней продолжительности жизни', age > ale)
print('Ваш возраст меньше или равен средней продолжительности жизни', age <= ale)
print('Ваш возраст больше или равен средней продолжительности жизни', age >= ale)
print('У вас юбилей!', age % 5 == 0)