import pymongo
from pymongo.errors import ServerSelectionTimeoutError, PyMongoError

def main():
    try:
        # Подключение к базе данных
        client = pymongo.MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
        db = client["myDatabase"]

        # Коллекция, в которой будут храниться данные
        collection = db["users_bot"]

        # Данные для сохранения
        user_id = 12345
        user_data = {
            '_id': user_id,  # Установка уникального идентификатора
            'warehouse_id': 1,  # Пример значения
            'warehouse_name': "Main Warehouse",  # Пример значения
            'max_coefficient': 100,  # Пример значения
            'box_type_name': "Standard",  # Пример значения
            'last_coefficients': {}  # Пустой словарь
        }

        # Вставка данных в коллекцию
        collection.insert_one(user_data)

        # Запрос данных по определенным критериям
        query = {"_id": user_id}  # Используем user_id
        result = collection.find_one(query)

        # Вывод полученных данных
        print(result)

    except ServerSelectionTimeoutError:
        print("Ошибка подключения к базе данных: сервер не доступен.")
    except PyMongoError as e:
        print(f"Произошла ошибка при работе с MongoDB: {e}")
    finally:
        # Закрытие соединения с базой данных
        client.close()

if __name__ == '__main__':
    main()