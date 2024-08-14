# Pythob with MongoDB
Проект практики по работе с базой данных MongoDB на языке Python

## Настройка
У вас должен уже быть установлен менеджер проектов Poetry и прокси-сервер Nginx.

Скачайте проект с GitHub
```bash
git clone https://github.com/rosoporto/example_mongodb.git
```

Установите зависимости:
```bash
poetry install
```

Создание конфигурационного файла для Nginx для вашего приложения:
```bash
sudo nano /etc/nginx/sites-available/yourproject
```

Вставьте следующую конфигурацию:your_domain_or_ip
```nginx
server {
    listen 80;
    server_name your_domain_or_ip; #Замените your_domain_or_ip на ваш домен или IP-адрес. 

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Создайте символическую ссылку для активации конфигурации:
```bash
sudo ln -s /etc/nginx/sites-available/yourproject /etc/nginx/sites-enabled
```

Проверка конфигурации Nginx: нет ли ошибок в конфигурации:
```bash
sudo nginx -t
```

Перезапуск Nginx: Перезапустите Nginx, чтобы применить изменения:
```bash
sudo systemctl restart nginx
```

## Запуск
В папке проекта запустите проект командой:
```bash
make server
```

Для демонстрации проекта на REST API запустите проект командой:
```bash
make api_server
```
Протестировать работу REST IP вы можете с использованием Postman или curl:

Добавление элемента:
```bash
curl -X POST http://127.0.0.1:5000/items -H "Content-Type: application/json" -d '{"name": "Test Item", "value": 42}'
```

Получение всех элементов:
```bash
curl -X GET http://127.0.0.1:5000/items
```

Получение конкретного элемента:
```bash
curl -X GET http://127.0.0.1:5000/items/Test Item
```

Обновление элемента:
```bash
curl -X PUT http://127.0.0.1:5000/items/Test Item -H "Content-Type: application/json" -d '{"value": 100}'
```

Удаление элемента:
```bash
curl -X DELETE http://127.0.0.1:5000/items/Test Item
```
