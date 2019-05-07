
import math


def greeting(name):
    if name is "Ago":
        return None
    return "Hello, " + name


def formula(n):
    return math.floor((n / 5) - (n % 3))


def what_meal(sleepy, food_ready):
    if sleepy is True and food_ready is False:
        return "breakfast"
    elif not sleepy and food_ready is True:
        return "lunch"
    elif sleepy and food_ready is True:
        return "dinner"
    return "no food for you"

def sum_ood(n):
    sum = 3
    for i in range(0
            , n, 2):
        sum = sum + i
    return sum



def capitalize2(word):
    return word[0:2].upper() + word[2:]


def remove_middle(numbers):
    # new_list = []
    # for i in range(len(numbers)):
    #     if i != len(numbers) / 2:
    #         new_list.append(numbers[i])
    # return new_listprint("--------------")
    pass

    numbers.pop((len(numbers) -1) // 2)
    return numbers




if __name__ == '__main__':

    print(greeting("Ago"))
    print(greeting("Märten"))
    print("--------------")
    print(formula(8))
    print("--------------")
    print(what_meal(False, True ))
    print("--------------")
    print(sum_ood(5))
    print("--------------")
    print(capitalize2("tere"))
    print("--------------")
    print(remove_middle([1, 2, 3]))
