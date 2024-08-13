# Pythob with MongoDB
Проект практики по работе с базой данных MongoDB на языке Python

## Настройка
У вас должен уже быть установлен менеджер проектов Poetry и прокси-сервер Nginx.

Скачайте проект с GitHub
```bash
git clone ...
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