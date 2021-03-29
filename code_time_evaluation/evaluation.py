import timeit
import time
import cProfile
from random import randrange


def execution_time(func):
    """
    Return info about time that was needed to execute func (like print(timeit.timeit(func)))
    :param func:
    :return:
    """

    def the_wrapper_around_the_original_function(*args, **kwargs):
        t_start = time.time()

        func(*args, **kwargs)

        time.sleep(2)
        t_end = time.time()
        res = round(t_end - t_start, 15)

        print("Time of the func execution: " + str(res))

    return the_wrapper_around_the_original_function


@execution_time
def fff():
    L = [randrange(10000) for i in range(1000)]
    return 42 in L or 43 in L or 333 in L


@execution_time
def fff2():
    L = [randrange(10000) for i in range(1000)]
    S = set(L)
    return 42 in S or 43 in S or 333 in S


@execution_time
def some_f() -> int:
    """
    Some useless function
    :return: x
    """
    x = 0
    x += 2
    x *= 5
    return x


def edge_values(some_list) -> str:
    """
    Return info about the best and the worst variants among list values
    :param some_list: list with values
    :return: str
    """
    best_var = worst_var = some_list[0]
    for i in range(len(some_list)):
        if some_list[i] < best_var:
            best_var = some_list[i]
        elif some_list[i] > worst_var:
            worst_var = some_list[i]
    return "Best var: " + str(best_var) + "; Worst var: " + str(worst_var) + "."


def evaluation():
    """
    pseudo main
    """

    s1 = """
    x = []
    for i in range(9999):
        x.append(i)
         """
    s2 = "x = []\nfor i in range(9999):\n    x.append(i)"
    s3 = "x = [i for i in range(9999)]"

    print("First experiment:")
    tries = timeit.repeat(s1, number=100)
    print(edge_values(tries))

    print("\nSecond experiment:")
    tries = timeit.repeat(s2, number=100)
    print(edge_values(tries))

    print("\nThird experiment:")
    tries = timeit.repeat(s3, number=100)
    print(edge_values(tries))

    print("\nFourth_experiment:")
    some_f()

    print("\nfifth_experiment:")
    cProfile.run("some_f()")

    print("\nsixth_experiment:")
    print("list var:")
    fff()
    print("set var:")
    fff2()
