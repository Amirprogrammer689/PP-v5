import os
import shutil
import csv
import re

def copy_dataset():

    '''
    Копирует файлы из датасета в новую директорию.
    '''

    dataset_path = os.path.abspath("dataset")

    if not os.path.exists("copy_dataset"):
        os.makedirs("copy_dataset")
    copy_dataset_path = os.path.abspath("copy_dataset")

    for root, dirs, files in os.walk(dataset_path):
        for filename in files:
            class_name = os.path.basename(root)
            class_name = class_name.replace(" ", "_")
            new_filename = f"{class_name}_{filename}"
            original_path = os.path.join(root, filename)
            new_path = os.path.join(copy_dataset_path, new_filename)
            shutil.copy(original_path, new_path)

def create_annotation_of_copy_dataset():

    '''
    Функция, которая создает аннотации(annotations_2.scv) для copy_dataset
    '''

    dataset_path = os.path.abspath("copy_dataset")

    with open('annotations_2.csv', 'w') as file:
        writer = csv.writer(file)
        for root, dirs, files in os.walk(dataset_path):
            for filename in files:
                absolute_path = os.path.abspath(os.path.join(root, filename))
                relative_path = os.path.relpath(absolute_path)
                class_name = os.path.basename(absolute_path)
                class_name = re.sub("_\d{4}.jpg", '', class_name)
                writer.writerow([absolute_path, relative_path, class_name])

def main():
    copy_dataset()
    create_annotation_of_copy_dataset()

if __name__ == "__main__":
    main()