# Напишите программу, которая определит позицию второго вхождения строки в списке,
# либо сообщит, что её нет.

def my_func(lst, find_str):
    if lst.count(find_str) > 1:
        k = lst.index(find_str)
        print(lst.index(find_str, k+len(find_str)))
    else:
        print('нет второго вхождения')


lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
f = "qwe"
my_func(lst, f)
lst = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
f = "йцу"
my_func(lst, f)
lst = ["йцу", "фыв", "ячс", "цук", "йцукен"]
f = "йцу"
my_func(lst, f)
lst = ["123", "234", 123, "567"]
f = "123"
my_func(lst, f)
lst = []
f = "123"
my_func(lst, f)
