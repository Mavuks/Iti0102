"""Order names by popularity."""
from collections import Counter

def read_from_file() -> list:
    """
    Create the list of all the names.

    :return: list
    """
    names = []
    with open("popular_names.txt", encoding='utf-8') as file:
        for line in file:
            names.append(line.strip())
    return names


def to_dictionary(names: list) -> dict:
    """
    Make a dictionary from a list of names.

    :type names: object
    :param names: list of all the names
    :return: dictionary {"name:sex": number}
    """

    names_dict = {}
    for name in names:
        if any(name in s for s in names_dict):
            continue
        else:
            names_dict.update({str(name): names.count(name)})
    return names_dict

    #for i in range(len(names)):
    #    names_dict[names[i]] = names.count(names[i])
    #return names_dict


def to_sex_dicts(names_dict: dict) -> tuple:
    """
    Divide the names by sex to 2 different dictionaries.

    :param names_dict: dictionary of names
    :return: two dictionaries {"name": number}, {"name": number}
    first one is male names, seconds is female names.
    """
    pass
    male_names = {}
    female_names = {}
    for name, count in names_dict.items():
        if any(':M' in s for s in names_dict):
            male_names.update({str(name[:-2]): count})
        elif any(':F' in s for s in names_dict):
            female_names.update({str(name[:-2]): count})

    return male_names, female_names




def most_popular(names_dict: dict) -> str:
    """
    Find the most popular name in the dictionary.

    If the dictionary is empty, return "Empty dictionary."
    :param names_dict: dictionary of names (key is name, value is count)
    :return: string
    """
    return Counter(names_dict).most_common(1)




def number_of_people(names_dict: dict) -> int:
    """
    Calculate the number of people in the dictionary.

    :param names_dict: dictionary of names (key is name, value is count)
    :return: int
    """
    pass
    return int(sum(names_dict.values()))


def names_by_popularity(names_dict: dict) -> str:
    r"""
    Create a string used to print the names by popularity.

    Format:
        1. name: number of people + "\n"
        ...

    Example:
        1. Kati: 100
        2. Mati: 90
        3. Nati: 80
        ...

    :param names_dict: dictionary of the names (key is name, value is count)
    :return: string
    """
    pass





if __name__ == '__main__':
    example_names = ("Kati:F\n" * 1000 + "Mati:M\n" * 800 + "Mari:F\n" * 600 + "Tõnu:M\n" * 400).rstrip("\n").split("\n")
    people = to_dictionary(example_names)
    print(people)  # -> {'Kati:F': 1000, 'Mati:M': 800, 'Mari:F': 600, 'Tõnu:M': 400}
    male_names, female_names = to_sex_dicts(people)
    print(male_names)  # -> {'Mati': 800, 'Tõnu': 400}
    print(female_names)  # -> {'Kati': 1000, 'Mari': 600}
    print(most_popular(male_names))  # -> "Mati"
    print(number_of_people(people))  # -> 2800
    print(names_by_popularity(male_names))  # ->   1. Mati: 800
#                                                  2. Tõnu: 400
#                                                  (empty line)
