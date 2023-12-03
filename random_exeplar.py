import os

def get_next(class_name) -> str:
    path = os.path.join('dataset', class_name)
    class_names = os.listdir(path)
    for i in range (len(class_names)):
        if class_names[i] is not None:
            print(os.path.join(path, class_names[i]))
        else:
            return None
    
def main():
    get_next("brown bear")
    get_next("polar bear")

if __name__ == "__main__":
    main()