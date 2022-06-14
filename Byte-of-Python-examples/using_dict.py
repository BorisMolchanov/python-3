# 'ab' - сокращение от 'a'ddress'b'ook

ab = { 'Swaroop' : 'swaroop@swaroopch.com',
		'Larry' : 'larry@wall.org',
		'Matsumoto' : 'matz@ruby-lang.org',
		'Spammer' : 'spammer@hotmail.com' }

print("Адрес Swaroop'а:", ab['Swaroop'])

# Удаление пары ключ-значение
del ab['Spammer']

print('\nВ адресной книге {0} контакта\n'.format(len(ab)))

for name, address in ab.items():
	print('Контакт {0} с адресом {1}'.format(name, address))

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
	print("\nАдрес Guido:", ab['Guido'])