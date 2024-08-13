from pymongo import MongoClient


# Подключение к MongoDB
client = MongoClient("mongodb://localhost:27017/")


# Выбор или создание базы данных
db = client["myDatabase"]


# Создание коллекций
users = db["users"]
products = db["products"]
orders = db["orders"]
reviews = db["reviews"]
categories = db["categories"]


# Добавление документов
users.insert_one({
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
})


products.insert_many([
    {"name": "Laptop", "price": 1200, "category": "electronics"},
    {"name": "Smartphone", "price": 800, "category": "electronics"},
    {"name": "T-Shirt", "price": 20, "category": "clothing"}
])


def main():
    # Аналитические запросы
    # Получение всех пользователей
    all_users = users.find()
    print(f"all_users: {list(all_users)}")


    # Получение всех продуктов в категории "electronics"
    electronics_products = products.find({"category": "electronics"})
    print(f"electronics_products: {list(electronics_products)}")


    # Подсчет количества всех заказов
    total_orders = orders.count_documents({})
    print(f"total_orders: {total_orders}")


    # Средняя цена продуктов
    average_price = products.aggregate([
        {"$group": {"_id": None, "averagePrice": {"$avg": "$price"}}}
    ])
    print(f"average_price: {list(average_price)}")


    # Список категорий продуктов и количества продуктов в каждой категории
    product_categories = products.aggregate([
        {"$group": {"_id": "$category", "count": {"$sum": 1}}}
    ])
    print(f"product_categories: {list(product_categories)}")


if __name__ == "__main__":
    main()
