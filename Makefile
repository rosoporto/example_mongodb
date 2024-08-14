server:
	poetry run gunicorn --workers=4 --bind=127.0.0.1:8080 mongodb.app:app
	
api_server:
	poetry run gunicorn --workers=4 --bind=127.0.0.1:8080 mongodb.app_api:app
