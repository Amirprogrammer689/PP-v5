import os
import csv

def create_annotation():
    
    '''
    Функция, которая создает аннотации(annotations.csv) для dataset
    '''

    dataset_path = os.path.abspath("dataset")

    with open('annotations.csv', 'w') as file:
        writer = csv.writer(file)
        for root, dirs, files in os.walk(dataset_path):
            for filename in files:
                absolute_path = os.path.abspath(os.path.join(root, filename))
                relative_path = os.path.relpath(absolute_path)
                class_name = os.path.basename(os.path.dirname(absolute_path))
                writer.writerow([absolute_path, relative_path, class_name])
   


def main():
    create_annotation()

if __name__ == "__main__":
    main()