import os
import shutil

root_folder_path = "путь к проекту 3"

def sort_images(root_folder_path):
    for folder_name in os.listdir(root_folder_path):
        folder_path = os.path.join(root_folder_path, folder_name)
        if os.path.isdir(folder_path):
            for subfolder_name in os.listdir(folder_path):
                subfolder_path = os.path.join(folder_path, subfolder_name)
                if os.path.isdir(subfolder_path):
                    for image_name in os.listdir(subfolder_path):
                        image_path = os.path.join(subfolder_path, image_name)
                        if os.path.isfile(image_path):
                            new_folder_name = os.path.splitext(image_name)[0]
                            new_folder_path = os.path.join(folder_path, new_folder_name)
                            os.makedirs(new_folder_path, exist_ok=True)
                            new_image_path = os.path.join(new_folder_path, image_name)
                            if image_path != new_image_path:
                                shutil.copy2(image_path, new_image_path)
                            # Удаляем исходный файл после копирования, если нужно
                            os.remove(image_path)
                    # Удаляем старую папку после копирования
                    shutil.rmtree(subfolder_path)

sort_images(root_folder_path)
