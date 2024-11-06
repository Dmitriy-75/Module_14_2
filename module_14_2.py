                            # Задача "Средний баланс пользователя":

import sqlite3
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Удалите из базы данных not_telegram.db запись с id = 6.
cursor.execute('DELETE FROM User WHERE id=?', (6,))

# Посчитать сумму всех балансов.
cursor.execute('SELECT SUM(balance) FROM User')
all_balances = cursor.fetchone()[0]
print(f'\nСумму всех балансовa = {all_balances}')

# Подсчитать общее количество записей.
cursor.execute('SELECT COUNT(*) FROM User')
total_users = cursor.fetchone()[0]
print(f'Общее количество записей = {total_users}')

# Вывести в консоль средний баланс всех пользователей
print(f'Средний баланс всех пользователей = {all_balances / total_users}')

connection.commit()
connection.close()












