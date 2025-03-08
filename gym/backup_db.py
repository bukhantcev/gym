import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


# Настройки
YANDEX_DISK_URL = "https://webdav.yandex.ru"
YANDEX_LOGIN = os.getenv("YANDEX_LOGIN")
YANDEX_PASSWORD = os.getenv("YANDEX_PASSWORD")
DB_PATH = "/root/gym/gym/db.sqlite3"  # Путь к базе
BACKUP_FOLDER = "backups"  # Папка на Яндекс.Диске
MAX_BACKUPS = 30  # Сколько бэкапов хранить

# Формируем имя файла бэкапа с датой
backup_filename = f"db_backup_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.sqlite3"

# Загружаем файл на Яндекс.Диск
with open(DB_PATH, "rb") as file:
    response = requests.put(
        f"{YANDEX_DISK_URL}/{BACKUP_FOLDER}/{backup_filename}",
        auth=(YANDEX_LOGIN, YANDEX_PASSWORD),
        data=file
    )

# Проверяем результат загрузки
if response.status_code == 201:
    print(f"✅ Бэкап успешно загружен: {backup_filename}")
else:
    print(f"❌ Ошибка загрузки: {response.status_code} - {response.text}")
    exit()

# Получаем список бэкапов на Яндекс.Диске
# Запрашиваем список файлов в папке backups
response = requests.request(
    "PROPFIND",
    f"{YANDEX_DISK_URL}/{BACKUP_FOLDER}/",
    auth=(YANDEX_LOGIN, YANDEX_PASSWORD),
    headers={"Depth": "1"}  # Указываем глубину запроса (нужен список файлов в папке)
)

if response.status_code == 207:  # 207 Multi-Status - успешный ответ WebDAV
    # Парсим список файлов
    backups = [item for item in response.text.split('<d:href>') if 'db_backup' in item]
    backups = [item.split('</d:href>')[0].split('/')[-1] for item in backups]

    # Сортируем по дате (новые бэкапы в конце)
    backups.sort()

    # Удаляем старые бэкапы, если их больше MAX_BACKUPS
    while len(backups) > MAX_BACKUPS:
        old_backup = backups.pop(0)
        delete_response = requests.delete(f"{YANDEX_DISK_URL}/{BACKUP_FOLDER}/{old_backup}", auth=(YANDEX_LOGIN, YANDEX_PASSWORD))
        if delete_response.status_code == 204:
            print(f"🗑 Удален старый бэкап: {old_backup}")
        else:
            print(f"❌ Ошибка удаления {old_backup}: {delete_response.status_code} - {delete_response.text}")

else:
    print(f"❌ Ошибка получения списка бэкапов: {response.status_code} - {response.text}")
