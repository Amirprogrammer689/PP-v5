import os
import shutil
import csv
import random
import re

def get_new_path(class_name, copy_dataset_path):

    '''
    Генерирует новый путь для файла из указанного класса в новом датасете.

    Args:
        class_name (str): Название класса.
        copy_dataset_path (str): Путь к новому датасету.

    Returns:
        str: Новый путь для файла из указанного класса в новом датасете.
    '''

    random_filename = f"{random.randint(0, 10000)}.jpg"
    new_filename = f"{class_name}_{random_filename}"
    new_filename = re.sub("\D{5}_\D{4}_", '', new_filename)
    new_path = os.path.join(copy_dataset_path, new_filename)
    return new_path

def create_dataset_random_and_annotations():

    '''
    Создает новый датасет с копиями файлов из исходного датасета и генерирует файл аннотаций.
    '''

    dataset_path = os.path.abspath("dataset")

    if not os.path.exists("dataset_random"):
        os.makedirs("dataset_random")
    copy_dataset_path = os.path.abspath("dataset_random")

    with open('annotations_3.csv', 'w') as file:
        writer = csv.writer(file)

        for root, dirs, files in os.walk(dataset_path):
            for filename in files:
                class_name = os.path.basename(root)
                class_name = class_name.replace(" ", "_")
                original_path = os.path.join(root, filename)
                new_path = get_new_path(class_name, copy_dataset_path)
                while os.path.exists(new_path):
                    new_path = get_new_path(class_name, copy_dataset_path)

                shutil.copy(original_path, new_path)

                relative_path = os.path.relpath(new_path)
                writer.writerow([new_path, relative_path, class_name])

def main():
    
    '''
    Точка входа в программу. Вызывает функцию для создания нового датасета и генерации файлов аннотаций.
    '''

    create_dataset_random_and_annotations()

if __name__ == "__main__":
    main()