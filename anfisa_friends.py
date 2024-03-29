'''
.
Анфиса уже умеет отвечать на вопрос «Сколько у меня друзей?»: при вызове функции process_anfisa() она проверяет, равна ли строка query строке Сколько у меня друзей?, и если равна — получает длину словаря DATABASE и возвращает ответ.
В этом задании ваша цель — научить Анфису отвечать на вопрос «Кто все мои друзья?». Ответ Анфисы должен быть примерно таким:
# Имена должны разделяться пробелом; 
# в перечне должны быть все имена друзей из словаря DATABASE.
Твои друзья: Толя Андрей Коля Лера 
Добавьте в ветвление if...else инструкцию elif. В ней аргумент query надо сравнить со строкой 'Кто все мои друзья?'. 
Если переменная query содержит строку 'Кто все мои друзья?', то:
переберите в цикле словарь DATABASE и каждый ключ словаря (имя друга) добавьте в переменную friends_string — она уже объявлена в коде. Имена должны разделяться пробелом. Похожую операцию вы выполняли в уроке «Счётчики»;
с помощью инструкции return верните из функции строку, составленную из строки 'Твои друзья: ' и переменной friends_string. Здесь пригодится сложение строк, конкатенация.
'''

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return 'У тебя ' + str(count) + ' друзей.'
    # Здесь проверьте, что переменная query равна строке 'Кто все мои друзья?'
    elif query ==   'Кто все мои друзья?':
        friends_string = ''
        # Чтобы получить перечень друзей - 
        # переберите словарь DATABASE в цикле
        for friend in DATABASE :     
             friends_string += f'{friend} '     # Добавляйте к переменной friends_string имя друга и пробел
        # Верните строку, составленную из 'Твои друзья: ' и friends_string 
        return f'Твои друзья: {friends_string}'
    else:
        return '<неизвестный запрос>'

# Не изменяйте следующий код
print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
