import random
from code_time_evaluation.evaluation import execution_time


@execution_time
def bubble_sort_1(nums):
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True


@execution_time
def bubble_sort_2(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True


random_list_of_nums1 = [random.randint(1, 100) for _ in range(1000)]
random_list_of_nums2 = random_list_of_nums1.copy()
random_list_of_nums3 = random_list_of_nums1.copy()
random_list_of_nums4 = random_list_of_nums1.copy()
random_list_of_nums5 = random_list_of_nums1.copy()
random_list_of_nums6 = random_list_of_nums1.copy()

bubble_sort_1(random_list_of_nums1)
print(random_list_of_nums1)
print("______")
print("Bubble Sort #1:")
bubble_sort_1(random_list_of_nums2)
print("Bubble Sort #2:")
bubble_sort_2(random_list_of_nums3)
