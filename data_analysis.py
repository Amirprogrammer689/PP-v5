import csv
import typing
import pandas as pd
import cv2 
import random
import matplotlib.pyplot as plt

def read_file(path: str) -> list[list[str]]:
    '''
    Читает файл CSV и возвращает список списков, содержащих пути к файлам и классы.

    Аргументы:
    path (str): Путь к файлу CSV.

    Возвращает:
    list[list[str]]: Список списков, содержащих пути к файлам и классы.
    '''
    files: list[list[str]] = []
    with open(path, "r") as csvfile:
        reader: csv.DictReader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            files.append([row["full_path"], row["class"]])
    return files

#чтение файла
list_file_info: list[list[str]] = read_file("annotations_1.csv")

# task 1
df_two_columns = pd.DataFrame(columns=["Name", "AbsPath"])
for file_info in list_file_info:
    df_two_columns.loc[len(df_two_columns)] = [file_info[1], file_info[0]]
print(df_two_columns.head(5))

# task 2-4
df = pd.DataFrame(columns=["Name", "AbsPath", "ClassId", "Weight", "Height", "Depth"])
for file_info in list_file_info:
    class_id = 0 if file_info[1] == "brown bear" else 1
    im = cv2.imread(file_info[0])
    h, w, c = im.shape
    df.loc[len(df)] = [file_info[1], file_info[0], class_id, w, h, c]
print(df.head(5))

