def data_types():
    num = 10
    word = "apple"
    numf = 10.1
    boolean = True
    empty_list = []
    grade = {"Alex": 5, "Misha": 3}
    fruits = ("apple", "banana")
    numbers = {1, 2, 3, 2, 1}
    print(f"[{type(num).__name__}, {type(word).__name__}, {type(numf).__name__}, {type(boolean).__name__}, {type(empty_list).__name__}, {type(grade).__name__}, {type(fruits).__name__}, {type(numbers).__name__}]")
if __name__ == '__main__':
    data_types()