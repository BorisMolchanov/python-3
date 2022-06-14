try:
	text = input('Введите что-нибудь --> ')
except EOFError:
	print('Ну зачем вы сделали мне EOF?')
except KeyboardInterrupt:
	print('Вы отменили операцию.')
else:
	print('Вы ввели {0}'.format(text))