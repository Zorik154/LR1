import os
import subprocess

# Папка будущего репозитория
repo_path = "my_local_repo"

# Создаём папку, если её нет
os.makedirs(repo_path, exist_ok=True)

# Переходим в неё
os.chdir(repo_path)

# Инициализируем Git-репозиторий
subprocess.run(["git", "init"])

# Создаём файл
with open("README.md", "w", encoding="utf-8") as f:
    f.write("# Мой локальный Git репозиторий\n")

# Добавляем файл в индекс
subprocess.run(["git", "add", "README.md"])

# Делаем коммит
subprocess.run(["git", "commit", "-m", "Первый коммит"])