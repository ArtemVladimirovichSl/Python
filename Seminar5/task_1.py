# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.

def get_data_from_file(nums):
    data = open(nums, 'r')
    dlist = data.read() + ' '
    dlist = list(map(int, dlist.split()))
    data.close()
    return dlist


def find_number(nums):
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] > 1:
            return nums[i] + 1


nums_list = get_data_from_file('natural_numbers.txt')

print('Числа из файла:', *nums_list)
print('Недостающее число:', find_number(nums_list))


def get_full_nums(nums):                    # Добавляем недостающее число в список
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] > 1:
            nums.insert(i+1, nums[i] + 1)
    return nums


nums = get_data_from_file('natural_numbers.txt')
