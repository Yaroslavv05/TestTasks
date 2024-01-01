# Базовый образ - Python
FROM python

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в рабочую директорию контейнера
COPY . .

# Установка зависимостей (если есть requirements.txt)
RUN pip install -r requirements.txt

# Запускаем скрипт для выполнения тестов
CMD ["bash", "run.sh"]
