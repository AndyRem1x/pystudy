class Mathematician:
    @staticmethod
    def square_nums(int_list):
        return [number**2 for number in int_list]

    @staticmethod
    def remove_positives(int_list):
        return [number for number in int_list if number < 0]

    @staticmethod
    def filter_leaps(int_list):
        return [num for num in int_list if num % 4 == 0]


mathematician_1 = Mathematician()

assert mathematician_1.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert mathematician_1.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert mathematician_1.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
