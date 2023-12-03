import os
class Iterator:
    def __init__(self, class_name):
        self.class_name = class_name
        self.data = os.listdir(os.path.join('dataset', self.class_name))
        self.limit = len(self.data)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return os.path.join(self.class_name, self.data[self.counter])
        else:
            raise StopIteration



def main():
    brown_bear=Iterator('brown bear')
    polar_bear=Iterator('polar bear')
    
    print(next(brown_bear))
    print(next(polar_bear))
    print(next(brown_bear))
    print(next(polar_bear))
    print(next(brown_bear))
    print(next(polar_bear))
    print(next(brown_bear))
    print(next(polar_bear))
    print(next(brown_bear))
    print(next(polar_bear))
    print(next(brown_bear))
    print(next(polar_bear))
    print(next(brown_bear))
    print(next(polar_bear))
    print(next(brown_bear))

if __name__ == "__main__":
    main()