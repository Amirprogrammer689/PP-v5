import csv
import pandas as pd
import cv2 
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
'''
Создает новый DataFrame "df_two_columns" с двумя столбцами "Name" и "Absolute Path". 
Затем проходит по каждому элементу в `list_file_info` и добавляет строку в DataFrame, используя значения из `file_info`. 
'''
df_two_columns = pd.DataFrame(columns=["Name", "Absolute Path"])
for file_info in list_file_info:
    df_two_columns.loc[len(df_two_columns)] = [file_info[1], file_info[0]]
print(df_two_columns.head(5))

# task 2-4
'''
Создает новый DataFrame "df" с шестью столбцами: "Name", "Absolute Path", "Class Id", "Width", "Height", "Depth".
Затем проходит по каждому элементу в `list_file_info` и добавляет строку в DataFrame, используя значения из `file_info`.
Для каждого файла определяется значение `class_id` на основе условия.
После этого изображение читается с использованием OpenCV, и его размеры сохраняются в переменные h, w, c.
'''
df = pd.DataFrame(columns=["Name", "Absolute Path", "Class Id", "Width", "Height", "Depth"])
for file_info in list_file_info:
    class_id = 0 if file_info[1] == "brown bear" else 1
    im = cv2.imread(file_info[0])
    h, w, c = im.shape
    df.loc[len(df)] = [file_info[1], file_info[0], class_id, w, h, c]
print(df.head(5))

# task 5
'''
Создает static_info, содержащий средние значения высоты, ширины, глубины и идентификатора класса из DataFrame df.
'''
static_info = {"Height": df["Height"].mean(), "Width": df["Width"].mean(),
               "Depth":  df["Depth"].mean(), "Class Id": df["Class Id"].mean()}
print(static_info)

# task 6
'''
Создает новый DataFrame filtered_df, содержащий строки из df, где значение "Class Id" равно 1.
'''
filtered_df = df.loc[df["Class Id"] == 1]
print(filtered_df)

# task 7
'''
Создает новый DataFrame filtered_df_size, содержащий строки из df, где значение "Class Id" равно 1, а также ширина и высота меньше или равны 320.
'''
filtered_df_size = df.loc[(df["Class Id"] == 1) & (df["Width"] <= 320) & (df["Height"] <= 320)]
print(filtered_df_size)

# task 8
'''
Вычисляет количество пикселей для каждой строки в DataFrame и добавляет результат в новый столбец "Pixel Count".
Затем группирует DataFrame по "Class Id" и вычисляет максимальное, среднее и минимальное значение "Pixel Count" для каждой группы.
'''
df['Pixel Count'] = df['Height'] * df['Width'] * df['Depth']
grouped_df = df.groupby('Class Id')['Pixel Count'].agg(['max', 'mean', 'min'])
print(grouped_df)

# task 9
'''
Создает фильтр, который выбирает строки из DataFrame, где значение "Class Id" равно 0. Затем выбирает случайный путь из столбца "Absolute Path", считывает изображение с использованием OpenCV и разделяет его на каналы R, G, B.
'''
filter = df.loc[df["Class Id"] == 0]
path = filter["Absolute Path"].sample(1).values[0]
img = cv2.imread(path, cv2.IMREAD_COLOR)
r, g, b = cv2.split(img)

# task 10
'''
Строит гистограммы для каналов R, G, B изображения, используя 256 корзин для каждого канала, затем добавляет подписи к осям и заголовок и отображает гистограмму.
'''
plt.hist(r.ravel(), bins=256, color='#FF0000')
plt.hist(g.ravel(), bins=256, color='#00FF00')
plt.hist(b.ravel(), bins=256, color='#0000FF')

plt.xlabel("OX")
plt.ylabel("OY")
plt.title("histogramm")

plt.show()