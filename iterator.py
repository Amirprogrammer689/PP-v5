import csv
import typing
from typing import Optional

def read_file(path: str) -> list[list[str]]:
    '''Читает файл и возвращает матрицу имён файлов
    Parameters
    ----------
    path(str) : Путь к файлу
    Returns
    -------
    list[list[str]]
    Матрица имён файлов'''
    files: list[list[str]] = []
    with open(path, "r") as csvfile:
        reader: csv.DictReader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            files.append([row["full_path"], row["class"]])
    return files


class Iterator:
    '''Класс-итератор для получения полного пути к файлу'''
    def __init__(self, files_class: str, path: str) -> None:
        self.file_class: str = files_class
        csv_f: list[list[str]] = read_file(path)
        self.annotation: list[list[str]] = [i for i in csv_f if i[1] == self.file_class]

    def __next__(self) -> Optional[str]:
        if self.annotation:
            item_0: str = self.annotation[0][0]
            self.annotation: list[list[str]] = self.annotation[1:]
            return item_0
        else:
            return None


if __name__ == "__main__":
    path_to_annotation: str = "annotations_1.csv"
    fileIterator: Iterator = Iterator("brown bear", path_to_annotation)
    fileIterator: Iterator = Iterator("polar bear", path_to_annotation)
    while True:
        next_val: Optional[str] = next(fileIterator)
        print(next_val)
        if next_val is None:
          break
    