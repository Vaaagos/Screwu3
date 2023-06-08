import os
import shutil

# Путь к папке А
folder_A = 'путь к папке а'

# Создадим новые 10 папок для отсортированных картинок и вставимк ним путь
sorted_folder = 'путь/к/папке/с/отсортированными/картинками'
os.makedirs(sorted_folder, exist_ok=True)
sorted_folder = 'путь/к/папке/с/отсортированными/картинками'
os.makedirs(sorted_folder, exist_ok=True)
sorted_folder = 'путь/к/папке/с/отсортированными/картинками'
os.makedirs(sorted_folder, exist_ok=True)
sorted_folder = 'путь/к/папке/с/отсортированными/картинками'
os.makedirs(sorted_folder, exist_ok=True)
sorted_folder = 'путь/к/папке/с/отсортированными/картинками'
os.makedirs(sorted_folder, exist_ok=True)
sorted_folder = 'путь/к/папке/с/отсортированными/картинками'
os.makedirs(sorted_folder, exist_ok=True)
sorted_folder = 'путь/к/папке/с/отсортированными/картинками'
os.makedirs(sorted_folder, exist_ok=True)
sorted_folder = 'путь/к/папке/с/отсортированными/картинками'
os.makedirs(sorted_folder, exist_ok=True)
sorted_folder = 'путь/к/папке/с/отсортированными/картинками'
os.makedirs(sorted_folder, exist_ok=True)
sorted_folder = 'путь/к/папке/с/отсортированными/картинками'
os.makedirs(sorted_folder, exist_ok=True)
# Перебор папок 1, 2, 3
for subfolder in ['1', '2', '3']:
    subfolder_path = os.path.join(folder_A, subfolder)

    # Перебор картинок в каждой папке
    for filename in os.listdir(subfolder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Формирование нового имени файла с учетом порядка
            new_filename = f'{subfolder}_{filename}'

            # Путь к исходному файлу
            src_path = os.path.join(subfolder_path, filename)

            # Путь к новому файлу
            dest_path = os.path.join(sorted_folder, new_filename)

            # Копирование файла в новую папку с новым именем
            shutil.copy(src_path, dest_path)
