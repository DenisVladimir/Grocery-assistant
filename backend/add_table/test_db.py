import json
import psycopg2

if __name__ == "__main__":
    db_name = input('Введите название БД: ')
    name_user = input('ведите имя пользователя: ')
    password_user = input('Введите пароль: ')

    conn = psycopg2.connect(dbname=f'{db_name}',
                            user=f'{name_user}',
                            password=f'{password_user}',
                            host='db')

    print('Database opened successfully')
    cursor = conn.cursor()

    name_table = input('Введите имя таблицы: ')
    # Подключение к Json file
    with open('ingredients.json', encoding='utf-8') as f:
        d = json.load(f)
        ID = 1 # Айди продукта надо проверить может наччинается с 0
        for item in d:
            name = item['name']  # название продукта
            # еденица измерения продукта
            measurement_unit = item['measurement_unit']
            cursor.execute(f"INSERT INTO {name_table} VALUES ({ID}, '{name}', '{measurement_unit}')")
            ID += 1  # прибавления ID    
        print("Record inserted successfully")

    conn.commit()  # закрытие курсора
    conn.close()
