
"""Recursion vs loops."""


def loop_reverse(s: str) -> str:
    """
    Reverse a string using a loop.

    :param s: input string
    :return: reversed input string
    """
    a = ""
    for i in range(1, len(s) + 1):
        a += s[len(s) - i]
    return a


def recursive_reverse(s: str) -> str:
    """
    Reverse a string using recursion.

    :param s: input string
    :return: reversed input string
    """
    if s == "":
        return s
    else:
        return recursive_reverse(s[1:]) + s[0]


def loop_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using a loop.

    :param n: the last number to add to the sum
    :return: sum
    """
    sum = 0
    while(n > 0):
        sum += n
        n -= 1
    return sum


def recursive_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using recursion.

    :param n: the last number to add to the sum
    :return: sum
    """
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)


if __name__ == '__main__':
    print(loop_reverse("hello"))  # -> "olleh"
    print(recursive_reverse("A"))  # -> "A"
    print(recursive_reverse(""))  # -> ""
    print(recursive_reverse("Tere, olen Märten.."))
    print(loop_sum(3))  # -> 6
    print(recursive_sum(95))  # -> 4560
    print(recursive_sum(0))  # -> 0

#
# def reverse_numbers(elements):
#     """
#     Reverse numbers in list.
#
#     [123] => [321]
#     [100] => [1]
#     [1, 23] => [1, 32]
#
#     :param elements: list of non-negative ints
#     :return: list of ints
#     """
#     new_list = []
#     for i in elements:
#         new_list.append(int((str(i)[::-1])))
#     return new_list
#
#
# def multiply_elements(integers, number):
#     """
#     Given a list of integers, multiply every element with the number, if
#     the number is greater than the element. If the number is equal to the element, multiply
#     the element by 2.
#
#     :param integers: list of integers
#     :param number: integer
#     :return: list of multiplied elements
#     """
#     new_list = []
#     for i in integers:
#         if i < number:
#             new_list.append(i * number)
#         elif i == number:
#             new_list.append(i * 2)
#         else:
#             new_list.append(i)
#     return new_list
#
#
# def swap_subword(s, subword):
#     """
#     If subword exists in s, reverse that part of s and return the modified string. Otherwise return original s.
#
#     "abcde", "bc" => "acbde"
#     :param s: original string
#     :param subword: len(subword) > 0
#     :return:
#     """
#     return s.replace(subword, subword[::-1], 1)
#
#
# def oranges_for_last_child(oranges, children):
#     """
#     Oranges are divided equally to all the children.
#     Orange cannot be divided into smaller parts
#     (only whole orange an be given to a child).
#     All the remaining oranges (which cannot be divided anymore)
#     are given to the last child.
#     How many oranges does the last child get?
#     :param oranges: Number of oranges
#     :param children: Number of children
#     :return: The number of oranges for the last child
#     """
#     return oranges // children + oranges % children
#
#
# def word_repeat_separator(word, separator, count):
#     """Given two strings, word and a separator, return a string made of count occurrences of the word,
#     separated by the separator string.
#
#     :param word: 'count' times occurring string.
#     :param separator: separates 'word' from another 'word'
#     :param count: indicates how many times word has to be present in result.
#     :return: string made of count occurrences of the word,
#     separated by the separator string.
#     """
#     if count > 1:
#         return word + (separator + word) * (count - 1)
#     else:
#         return word * count
#
#
# def longest_substring(long_string, short_string):
#     """
#     Given two strings of different length, find the longest substring of the longer one which begins
#     with the shorter one. The first argument is always the longer string.
#
#     :param long_string: longer string
#     :param short_string: shorter string, length > 0
#     :return: longest substring of one string beginning with the other. None if not found.
#     """
#     if long_string.find(short_string) >= 0:
#         return long_string[long_string.index(short_string):]
#     else:
#         return None
#
#
# def multiply_integer_values_by_3(d):
#     """
#     Multiply all integer values in dictionary by 3.
#
#     :param d: dictionary, where keys are strings and values are strings or integers
#     :return: updated dictionary
#     """
#     new_dict = {}
#     for i in d:
#             new_dict[i] = d[i] * 3
#     return new_dict
#
#
# def common_elements(list_a, list_b):
#     """
#     Given two lists, return a list of elements that can be found in both
#     input lists. The elements can be in any order.
#
#     The data structure returned must be a list!
#
#     :param list_a: list
#     :param list_b: list
#     :return: list of elements found in list_a and list_b
#     """
#     new_list = []
#     for i in list_a:
#         for y in list_b:
#             if i == y:
#                 new_list.append(i)
#     return new_list
#
#
# def minimum_maximum_sum(nr_list: list) -> tuple:
#     """Given 5 positive integers, find the minimum and maximum
#     values that can be calculated by summing exactly
#     four of the five integers. Then return the respective minimum and
#     maximum values as a tuple.
#
#     :param nr_list: list of 5 positive integers
#     :return: tuple consisting of minimum value and maximum value in that order.
#     """
#     sorted_list = sorted(nr_list)
#     max_value = sum(sorted_list[1:])
#     min_value = sum(sorted_list[0:4])
#     return min_value, max_value
#
#
# def wish_good_luck(person_name):
#     """
#     Print the message "Good luck with your exam, PERSON_NAME!\n" to the console.
#
#     For example:
#     wish_good_luck("Carl") will print to the console "Good luck with your exam, Carl!\n".
#
#     NB!
#     print(...) function puts '\n' to the end automatically!
#     Don't put it by yourself!
#
#     :param person_name: Name of the person who will be wished good luck. String.
#     :return: None.
#     """
#     print("Good luck with your exam, " + person_name + "!")
#
#
# def assess_students(correct_answers, students_answers):
#     """
#     Check answers of all students and calculate their results.
#
#     You are given string with correct answers, where correct answers for each question are divided by commas.
#     Since it was a test, there are only 4 possible answers: A, B, C or D.
#
#     For example: "A,ABCD,CD"
#     The correct answer to the first question is A.
#     The correct answers to the second question: A, B, C or D. (all answers are correct)
#     The correct answers to the third question: C or D.
#
#     students_answers is the list of strings where each string is the answers of every student.
#
#     For example: ["ABC", "AA ", "A B"]
#     The first student's answers: 1: A, 2: B, 3: C.
#     The second student's answers: 1: A, 2: A, 3: No answer.
#     The third student's answers: 1: A, 2: No answer, 3: B.
#
#     Calculate the result of each student separately.
#     Each correct answer gives 1 point, wrong answer lowers the result by 1 point
#     and if there is no answer provided, then result does not change.
#
#     The result should be in percentage:
#
#     Result(%) = (Result(points) / Number of questions) * 100
#
#     If result in points is negative, the student gets 0%!
#
#     The student's result should be rounded to the nearest int (hint: use round(result))
#     and represented as a string in the following format:
#
#     "{result}%"
#     For example:
#     0p out of 10p -> 0 / 10 = 0       -> "0%"
#     2p out of 6p  -> 2 / 6  = 0,3333  -> "33%"
#     5p out of 10p -> 5 / 10 = 0.5     -> "50%"
#     4p out of 6p  -> 4 / 6  = 0,6666  -> "67%"
#     6p out of 6p  -> 6 / 6  = 1       -> "100%"
#
#     Assume that the input is always correct:
#         - There will be at least one question in the test.
#         correct_answers:
#          - Contains only letters 'A', 'B', 'C', 'D' and commas to separate questions.
#          - There will be no spaces, numbers or other symbols.
#         student_answers:
#          - List contains only non-empty string.
#          - Length is always more than 0.
#         elements of students_answers list:
#          - At least one element.
#          - Contains only letters 'A', 'B', 'C', 'D' and spaces.
#          - Length is always the same as the number of questions in the test.
#
#     :param correct_answers: String with correct answers.
#     :param students_answers: List with students answers.
#     :return: List with results, where each result is a string.
#     """
#     pass
#
#
# def get_pyramid_blocks_amount(lowest_level):
#     """
#     Get amount of blocks required to build the pyramid.
#
#     The topmost level has 1 block, the next level down has two blocks,
#     the next level has 3 blocks and so on.
#
#     Example of the pyramid that has 3 levels: ('-' represents a block)
#       -
#      - -
#     - - - <- lowest_level = 3
#
#     Solution should be recursive.
#     Do not use loops, multiplication or sum functions!
#
#     :param lowest_level: The lowest level of the pyramid. Integer.
#     :return: Amount of blocks required to build pyramid.
#              If lowest level is 0 or negative, return 0.
#     """
#     if lowest_level < 1:
#         return 0
#     elif lowest_level == 1:
#         return 1
#     else:
#         return get_pyramid_blocks_amount(lowest_level - 1) + lowest_level
#
# # OOP1
#
#
# class Robot:
#     """Robot class."""
#
#     def __init__(self, init_coords, move_step, max_moves_amount):
#         """
#         Constructor.
#
#         :param init_coords: Initial coordinates of robot as list. Robot has two coordinates: [x, y].
#         :param move_step: Length of each step. Replaced by 1 if it is smaller.
#         :param max_moves_amount: Maximum moves. Replaced by 1 if it is smaller.
#         """
#         self.init_coords = init_coords
#         self.move_step = move_step
#         self.max_moves_amount = max_moves_amount
#         if move_step < 1:
#             self.move_step = 1
#
#         if max_moves_amount < 1:
#             self.max_moves_amount = 1
#
#     def get_coords(self):
#         """
#         Return current coordinates of robot as list.
#
#         :return: List of coordinates [x, y].
#         """
#         return self.init_coords
#
#     def get_move_step(self):
#         """
#         Return length of each step.
#
#         :return: Length of each step as integer.
#         """
#         return self.move_step
#
#     def get_max_moves_amount(self):
#         """
#         Return maximum moves amount.
#
#         :return: Maximum moves amount as integer.
#         """
#         return self.max_moves_amount
#
#     def get_moves_amount(self):
#         """
#         Return moves amount the robot has already done.
#
#         :return: Moves amount as integer.
#         """
#         pass
#
#     def move(self, direction):
#         """
#         Make move and change coordinates depending on direction.
#
#         Possible directions and how they change coordinates:
#         N: y + 1. E: x + 1.
#         S: y - 1. W: x - 1.
#         NE: x + 1, y + 1.
#         NW: x - 1, y + 1.
#         SE: x + 1, y - 1.
#         SW: x - 1, y - 1.
#
#         NB! Consider that robot cannot move, if its current moves amount equals maximum moves amount.
#
#         :param direction: Direction where to move.
#         :return: True if robot can move, otherwise False.
#         """
#         pass
#
#
# # OOP2
#
# class Troll:
#     """Troll."""
#
#     def __init__(self, name, weight, height, health_points, stamina_points):
#         """
#         Constructor;
#
#         :param name: troll name.
#         :param weight: troll weight (t).
#         :param height: troll height (m).
#         :param health_points: troll health points (hp).
#         :param stamina_points: troll stamina points (sp).
#         """
#         self.name = name
#         self.weight = weight
#         self.height = height
#         self.health_points = health_points
#         self.stamina_points = stamina_points
#
#     def get_troll_attack_speed(self):
#         """
#         Get the troll attack speed (1-100), integer.
#
#         The heavier and higher the troll is, the slower it moves.
#         The troll speed is calculated using the following formula: 100 / (weight + height).
#         Assume that sum of weight and height is always non-negative and smaller or equal to 100.
#
#         EXAMPLE
#         --------------------------------------------
#         troll weight = 3
#         troll height = 20
#         then troll speed = 100 / (3 + 20) = 4.347 ~ 4. So the answer is 4.
#         --------------------------------------------
#
#         :return: troll attack speed, integer.
#         """
#         return 100 // (self.weight + self.height)
#
#     def get_troll_attack_power(self):
#         """
#         Get the troll attack power, integer.
#
#         The heavier and higher the troll is, the stronger it is.
#         The troll attack power is just the sum of its weight and height.
#
#         EXAMPLE
#         --------------------------------------------
#         troll weight = 5
#         troll height = 20
#         then troll attack power = 5 + 20 = 25
#         --------------------------------------------
#
#         :return: troll attack power, integer.
#         """
#         return self.weight + self.height
#
#     def get_troll_level(self):
#         """
#         Get the level of the troll (1-5), integer.
#
#         Each troll has a level, which indicates how dangerous it is in combat.
#         The troll level mostly depends on its hp, sp, speed and attack power.
#         The level of the troll is calculated using the following formula:
#
#         delta = (5 - 1) / (3000 - 500) = 0.0016
#         troll_power = (troll health points + troll stamina points + troll attack speed + troll attack power)
#
#         formula: 0.0016 * (troll_power - 3000) + 5, round down
#
#         EXAMPLE
#         --------------------------------------------
#         troll hp = 500
#         troll stamina = 300
#         troll atk speed = 4
#         troll atk power = 25
#
#         delta = 0.0016
#         troll power = (500 + 300 + 4 + 25) = 829
#
#         troll lvl = 0.0016 * (829 - 3000) + 5) = 1.53 ~= 1
#         --------------------------------------------
#
#         :return: troll lvl.
#         """
#         troll_power = self.health_points + self.stamina_points + Troll.get_troll_attack_power(self) + Troll.get_troll_attack_speed(self)
#         return (0.0016 * (troll_power - 3000) + 5) // 1
#
#     def get_name(self):
#         """
#         Getter.
#
#         :return: troll name.
#         """
#         return self
#
#     def get_weight(self):
#         """
#         Getter.
#
#         :return: troll weight.
#         """
#         return self.weight
#
#     def get_height(self):
#         """
#         Getter.
#
#         :return: troll height.
#         """
#         return self.height
#
#     def get_hp(self):
#         """
#         Getter.
#
#         :return: troll hp.
#         """
#         return self.health_points
#
#     def get_sp(self):
#         """
#         Getter.
#
#         :return: troll sp.
#         """
#         return self.stamina_points
#
#     def __str__(self):
#         """
#         String representation.
#
#         :return: f"Name: {troll name}, lvl: {troll lvl}"
#         """
#         return f"Name: {self}, 1v1: {Troll.get_troll_level()}"
#
#
# class Hunter:
#     """Troll hunter."""
#
#     def __init__(self, attack_power, intelligent=False):
#         """
#         Constructor.
#
#         :param attack_power: Attack power of the hunter.
#         :param intelligent: Says for itself.
#         """
#         self.attack_power = attack_power
#         self.intelligent = intelligent
#
#     def call_for_help(self):
#         """
#         If the hunter is intelligent, he can call for help.
#
#         Calling for help increases attack power by 10.
#         :return:
#         """
#         if self.intelligent is True:
#             self.attack_power += 10
#
#     def get_attack_power(self):
#         """
#         Getter.
#
#         :return: hunter's atk power.
#         """
#         return self.attack_power
#
#     def is_intelligent(self):
#         """
#         Getter.
#
#         :return: is hunter intelligent? Boolean.
#         """
#         return self.intelligent
#
#
# class Mission:
#     """Mission."""
#
#     def __init__(self, hunters, troll):
#         """
#         Constructor.
#
#         :param hunters: list of hunters obj
#         :param troll: troll obj
#         """
#         self.hunters = hunters
#         self.troll = troll
#
#     def hunt(self):
#         """
#         The hunters try to slay down the given troll.
#
#         The hunters succeed if their total attack power is bigger than troll lvl * 300.
#         If their total attack power is smaller than troll lvl * 300, troll kills the most powerful hunter and
#         all intelligent hunters call for help.
#         If after calling for help total attack power of hunters is still too low, hunters die and the mission is failed.
#
#         If hunters succeed to kill the troll, return true. In other case return false.
#
#         :return: boolean
#         """
#
#     def set_hunters(self, hunters):
#         """
#         Setter.
#
#         :param hunters: list of hunters obj
#         """
#
#     def set_troll(self, troll):
#         """
#         Setter.
#
#         Check if troll is Troll class obj and set. In other case do not do anything.
#
#         :param troll: Troll class obj
#         """
#
#     def get_troll(self):
#         """
#         Getter.
#
#         :return: troll
#         """
#         return self.troll
#
#
# if __name__ == '__main__':
#
#     assert reverse_numbers([1]) == [1]
#     assert reverse_numbers([123]) == [321]
#     assert reverse_numbers([123, 10]) == [321, 1]
#     assert reverse_numbers([0, 0]) == [0, 0]
#
#     assert multiply_elements([1, 2, 3, 4, 5], 4) == [4, 8, 12, 8, 5]
#     assert multiply_elements([1], 1000) == [1000]
#     assert multiply_elements([4, 4, 4, 4], 2) == [4, 4, 4, 4]
#
#     assert swap_subword("tere", "a") == "tere"
#     assert swap_subword("tere", "er") == "tree"
#     assert swap_subword("tere", "e") == "tere"
#     assert swap_subword("", "e") == ""
#     assert swap_subword("aaabaaabaaba", "aaab") == "baaaaaabaaba"
#
#     assert oranges_for_last_child(10, 1) == 10
#     assert oranges_for_last_child(4, 2) == 2
#     assert oranges_for_last_child(5, 2) == 3
#
#     assert word_repeat_separator("AAA", "", 1) == "AAA"
#     assert word_repeat_separator("AAA", "", 0) == ""
#     assert word_repeat_separator("abc", "XX", 2) == "abcXXabc"
#     assert word_repeat_separator("Hi", "-n-", 2) == "Hi-n-Hi"
#     assert word_repeat_separator("a", "B", 5) == "aBaBaBaBa"
#
#     assert longest_substring("lestakalakalkulaator", "kal") == "kalakalkulaator"
#     assert longest_substring("postkast", "k") == "kast"
#     assert longest_substring("longer", "shrt") is None
#
#     assert common_elements([1, 2, 3], [9, 3, 2]) in [[2, 3], [3, 2]]
#     assert common_elements(['a', 'b', 'c'], ['b', 'd']) == ['b']
#
#     assert multiply_integer_values_by_3({"cookies": 7, "apples": 5}) == {"cookies": 21, "apples": 15}
#     assert multiply_integer_values_by_3({"t": 2, "e": -3}) == {"t": 6, "e": -9}
#     assert multiply_integer_values_by_3({"t": 4, "e": "foo"}) == {"t": 12, "e": "foo"}
#
#     assert minimum_maximum_sum([0, 1, 0, 0, 0]) == (0, 1)
#     assert minimum_maximum_sum([5, 6, 2, 3, 12]) == (16, 26)
#     assert minimum_maximum_sum([42, 27, 42, 27, 42]) == (138, 153)
#
#     assert wish_good_luck("GoodBoy") is None
#     # Good luck with your exam, GoodBoy!
#
#     assert assess_students("A,B,C,D", ["ABCD", "ABCD", "ABCD", "ABCD"]) == ["100%", "100%", "100%", "100%"]
#     assert assess_students("A,B,C,D", ["DCBA", "DDDC", "DABC"]) == ["0%", "0%", "0%"]
#     assert assess_students("A,A,A,D,C,C", ["DAADCC", "AADCCC", " AADCC", "AA DCD"]) == ["67%", "33%", "83%", "50%"]
#     assert assess_students("C,D,C", [" D ", "C D"]) == ["33%", "0%"]
#     assert assess_students("AB,B,DA", ["CBA", "BBD", " BD", "ABD", "ABA", "BBA"]) == ["33%", "100%", "67%", "100%",
#                                                                                       "100%", "100%"]
#
#     assert get_pyramid_blocks_amount(-1) == 0
#     assert get_pyramid_blocks_amount(0) == 0
#     assert get_pyramid_blocks_amount(1) == 1
#     assert get_pyramid_blocks_amount(2) == 3
#     assert get_pyramid_blocks_amount(3) == 6
#     """
#     # ============ ROBOT 1 ============
#     robot = Robot([-2, 3], 1, 3)
#
#     assert robot.move("NE")
#     assert robot.move("NW")
#     assert robot.move("S")
#     assert robot.move("E") is False
#     assert robot.move("S") is False
#
#     assert robot.get_coords() == [-2, 4]
#     assert robot.get_moves_amount() == 3
#
#     # ============ ROBOT 2 ============
#     robot = Robot([0, 0], 5, 9999)
#
#     directions = ["S", "S", "E", "SE", "NW", "S", "NE"]
#
#     for direction in directions:
#         assert robot.move(direction)
#
#     assert robot.get_coords() == [10, -10]
#     assert robot.get_moves_amount() == len(directions)  # 7
#
#     # ============ ROBOT 3 ============
#     robot = Robot([0, 0], -5, -3)
#
#     assert robot.get_max_moves_amount() == 1
#     assert robot.get_move_step() == 1
#
#     assert robot.move("N")
#
#     assert robot.get_coords() == [0, 1]
#     assert robot.get_moves_amount() == 1
#     """
#     # OOP2
#     t1 = Troll("Small Ice troll", 3, 25, 500, 700)
#     t2 = Troll("Big Ice troll", 10, 40, 2000, 1500)
#     h = Hunter(100, True)
#     h1 = Hunter(122)
#
#     hunters1 = [Hunter(50), Hunter(30), Hunter(12)]
#     hunters2 = [Hunter(120), Hunter(99), Hunter(98)]
#     smart_hunters = [Hunter(0, True) for _ in range(50)]
#     hunters2 += smart_hunters
#
#     m = Mission(hunters=hunters1, troll=t1)
#
#     assert t1.get_height() == 25
#     assert t1.get_weight() == 3
#     assert t1.get_hp() == 500
#     assert t1.get_sp() == 700
#     assert t1.get_name() == "Small Ice troll"
#
#     assert t1.get_troll_attack_speed() == 3
#     assert t1.get_troll_attack_power() == 28
#     assert t2.get_troll_attack_power() == 50
#     assert t1.get_troll_level() == 2
#     assert t2.get_troll_level() == 5
#
#     assert str(t1) == "Name: Small Ice troll, lvl: 2"
#     assert str(t2) == "Name: Big Ice troll, lvl: 5"
#
#     assert h.get_attack_power() == 100
#     h.call_for_help()
#     assert h.get_attack_power() == 110
#     h1.call_for_help()
#     assert h1.get_attack_power() == 122
#     assert h.is_intelligent()
#
#     assert m.get_troll() == t1
#     assert not m.hunt()
#
#     m.set_hunters(hunters2)
#     assert m.hunt()
#
#     m.set_troll(t2)
#     assert not m.hunt()
#
#     import math
#
#
#     def camel_case_word_counter(input_string):
#         """
#         Given input_string of concatenation of one or more words consisting of English letters
#         where first word is lowercase and other words start with uppercase, count and return number
#         of words. In case of empty string, return zero.
#
#         #01
#
#         :param input_string: camel cased string.
#         :return: integer which shows number of words in camel cased string.
#         """
#         if input_string == '':
#             return 0
#
#         count = 1
#         for char in input_string:
#             if char.isupper():
#                 count += 1
#
#         return count
#
#
#     def search_backwards(string, letter):
#         """
#         Given a string and a letter, find the second last occurrence of the letter in the string
#         and return its index.
#
#         #02
#
#         :param string: string to search from
#         :param letter: letter to search for
#         :return: second last index of the letter in the string. -1 if not found.
#         """
#         count = string.count(letter)
#         if count < 2:
#             return -1
#
#         for _ in range(count - 2):
#             string = string.replace(letter, "", 1)
#
#         return string.index(letter) + (count - 2)
#
#
#     def beatles(song):
#         """
#         You are given a song name with publication year as a string.
#         Publication year is always 4 digits and is the last part of the input string.
#         There is always a space between the name and the year.
#         Song name has at least one symbol.
#         If the publication year is before 1970, return "*song name* is a Beatles song!"
#         otherwise return "*song name* is not a Beatles song!".
#
#         #03
#
#         @param: song with a song title and a publication year (last 4 digits).
#         Example: "Yellow Submarine 1966".
#         @return: String "Yellow Submarine is a Beatles song!" if a Beatles song is found or
#         "Gangnam Style is not a Beatles song!" if not a Beatles song.
#         """
#         song_name = song[:-5]
#         year = int(song[-4:])
#
#         if year < 1970:
#             return song_name + ' is a Beatles song!'
#         else:
#             return song_name + ' is not a Beatles song!'
#
#
#     def apple_sharing(apples, children):
#         """
#         Apples are divided equally to all the children.
#         Apple cannot be divided into smaller parts
#         (only whole apple can be given to a child).
#         After all the children have got equal number
#         of apples, the rest will be shared so that
#         some children get one more apple compared to others.
#         How many children have 1 less apple compared to others?
#         If everyone have equal number of apples, return 0.
#
#         #04
#
#         :param apples: Number of apples.
#         :param children: Number of children.
#         :return: Amount of children who have -1 apple
#         compared to others.
#         """
#         if apples % children == 0:
#             return 0
#         else:
#             return children - (apples % children)
#
#
#     def to_upper(word, letters):
#         """
#         Given two strings - a word and a group
#         of letters, change all the given letters
#         found in the word to upper-case.
#
#         #05
#
#         :param word: word to change
#         :param letters: letters to change
#         :return: result word
#         """
#         new_word = ''
#         for c in word:
#             if c in letters:
#                 new_word += c.upper()
#             else:
#                 new_word += c
#
#         return new_word
#
#
#     def lowercase_with_suffix(s, suffix):
#         """
#         Add a suffix to end of string and make the last 3 letters lowercase (after adding the suffix).
#
#         Total length of concatenated string is always at least 3.
#
#         #06
#
#         :param suffix: string of ascii letters
#         :param s: string of ascii letters
#         :return: string
#         """
#         result = s + suffix
#         return result[:-3] + result[-3:].lower()
#
#
#     def remove_bigger_than_last(numbers):
#         """
#         Remove numbers from list that are bigger than last element in list.
#
#         #07
#
#         :param numbers: list of numbers
#         :return: list
#         """
#         return list(filter(lambda x: x <= numbers[-1], numbers))
#
#
#     def multiplication(begin, end=0):
#         """
#         With a given integral numbers begin and end, write a program to generate a
#         dictionary that contains (i, i*i) by 1 or -1 step in such a way that numbers are
#         between begin and end (both included) parameters.
#         (the order of items in the dictionary is not important)
#
#         #08
#
#         :param begin: integer which is the first key in dictionary
#         :param end: integer which is the last key in dictionary
#         :return: dictionary as key:i, value:i*i
#         """
#         b = min(begin, end)
#         e = max(begin, end)
#
#         dictionary = dict()
#         for i in range(b, e + 1):
#             dictionary[i] = i * i
#
#         return dictionary
#
#
#     def increment_by_one(numbers, pad_with_zeros=False):
#         """
#         Increment each number in list by one.
#
#         If pad_zeros is True, make the list bigger by adding 0 to the front and back of list.
#
#         #09
#
#         :param numbers: list of numbers
#         :param pad_with_zeros: boolean
#         :return: list
#         """
#         new_list = list(map(lambda x: x + 1, numbers))
#         if pad_with_zeros:
#             new_list.insert(0, 0)
#             new_list.append(0)
#
#         return new_list
#
#
#     def fizz(divisor):
#         """
#         Print numbers from 0 to 20 (included) where number that can be divided by divisor is replaced by string 'fizz'.
#         Every number should go on it's own line (print() includes new line symbol by default, do NOT remove it)
#
#         Example:
#         if divisor is 3 print:
#         '0
#         1
#         2
#         fizz
#         4
#         5
#         fizz
#         7
#         ...
#         20
#         '
#
#         #10
#
#         :param divisor: if a number can be divided with this, replace it with 'fizz' in output
#         :return: None
#         """
#         for i in range(21):
#             if i % divisor == 0:
#                 print('fizz')
#             else:
#                 print(i)
#
#
#     def histogram(els):
#         """
#         Return a histogram of digits on the scale from 0 to 10.
#
#         The given string consists of digits.
#         The function should return a list where
#         every element represents one digit
#         (first element represents '0', the second '1' etc).
#         For every element the occurrence ratio compared to the maximum occurrence
#         is represented on the scale of 0 to 10 as '*'s.
#         The element which occurs the most, will have 10 '*'s etc.
#         When needed, round down
#         In case of empty input return empty histogram.
#
#         "1234567890112" =>
#         ['***', '**********', '******', '***', '***', '***', '***', '***', '***', '***']
#
#         '0': 1
#         '1': 3
#         '2': 2
#         '3'-'9': 1
#         max occurrence = 3
#         '0': 1 / 3 * 10 = 3
#         '1': 3 / 3 * 10 = 10
#         '2': 2 / 3 * 10 = 6
#         '3'-'9': 1/3 * 10 = 3
#
#         In the following examples, the numbers represents the numbers on '*'s:
#         1231
#         [0, 10, 5, 5, 0, ...]
#
#         123221
#         [0, 6, 10, 3, 0, ...]
#
#         9
#         [0, 0, ... 10]
#
#         111111111112
#         [0, 10, 0, ..]
#
#         0220
#         [10, 0, 10, 0, ...]
#
#         #11
#
#         :param els: string of digits
#         :return: histogram as list
#         """
#         occurrence = dict()
#         for num in els:
#             try:
#                 occurrence[num] += 1
#             except KeyError:
#                 occurrence[num] = 1
#
#         # Find max occurrence
#         max_occurrence = 0
#         for value in occurrence.values():
#             if value > max_occurrence:
#                 max_occurrence = value
#
#         # Create histogram
#         histo = list()
#         for num in range(10):
#             num = str(num)
#             try:
#                 histo.append(math.floor(occurrence[num] / max_occurrence * 10) * '*')
#             except KeyError:
#                 histo.append('')
#
#         return histo
#
#
#     def substring(string, count):
#         """
#         Return first part of string with length of count.
#         Function should be recursive, loops (for/while) are not allowed!
#         count <= len(string)
#
#         #12
#
#         :param string: str
#         :param count: int, count < len(string)
#         :return: first count symbols from string
#         """
#         if count <= 0:
#             return ""
#
#         return string[0] + substring(string[1:], count - 1)
#
#
#     # oop 1
#     # 13
#
#     class Bus:
#         """Class that defines bus object."""
#
#         def __init__(self, stations, seats):
#             """
#             Initialize bus.
#
#             :param stations: List of stations, where each station is a string. Always contains at least one element.
#             Some station may be in the list more than once, but identical stations will never be near to each other.
#
#             :param seats: Amount of seats for passengers. Integer. Replaced by 1 if smaller. Bus driver does not need a seat.
#             """
#             self.stations = stations
#             if seats < 1:
#                 seats = 1
#             self.seats = seats
#             self.passengers = 0
#             self.current_station_index = 0
#
#         def get_amount_of_people(self):
#             """
#             Return amount of people in the bus including bus driver.
#
#             Assume that driver is always in the bus.
#
#             :return: Amount of people as integer.
#             """
#             return self.passengers + 1
#
#         def register_new_passenger(self):
#             """
#             Register new passenger if there is a seat for him/her.
#
#             :return: True if passenger can pass, otherwise (if no more seats) False.
#             """
#             if self.seats - self.passengers > 0:
#                 self.passengers += 1
#                 return True
#             else:
#                 return False
#
#         def release_passenger(self):
#             """
#             Decrement amount of passengers by 1.
#
#             Is called when a passenger leaves the bus.
#
#             If there is no passengers, nothing should change.
#             """
#             if self.passengers > 0:
#                 self.passengers -= 1
#
#         def get_current_station(self):
#             """
#             Return the station there the bus is at the moment.
#
#             Consider that bus is never between two stations.
#
#             If bus has not moved yet, return the first station.
#
#             :return: Bus station name as string.
#             """
#             return self.stations[self.current_station_index]
#
#         def move_next(self):
#             """
#             Move to the next station.
#
#             Bus can move to the next station if only there is at least one passenger
#             (not driver) and there are stations to go.
#
#             :return: True if bus moved to the next station, otherwise False.
#             """
#             if self.passengers >= 1 and self.current_station_index + 1 < len(self.stations):
#                 self.current_station_index += 1
#                 return True
#             else:
#                 return False
#
#
#     # oop 2
#     # 14
#
#     class Piano:
#         """Represents the physical real-life object."""
#
#         def __init__(self, width, length, height, manufacturer):
#             """
#             Constructor.
#
#             :param width: The maximum width of the piano in centimeters.
#             :param length: The maximum length of the piano in centimeters.
#             :param height: The maximum height of the piano in centimeters.
#             :param manufacturer: The company that built the piano.
#             """
#             self.width = width
#             self.length = length
#             self.height = height
#             self.manufacturer = manufacturer
#
#         def get_dimensions(self):
#             """
#             Get the dimensions of the piano in centimeters.
#
#             :return: A tuple (width, length, height).
#             """
#             return self.width, self.length, self.height
#
#         def get_manufacturer(self):
#             """
#             Get the manufacturer of the piano.
#
#             :return: The company that built the piano.
#             """
#             return self.manufacturer
#
#
#     class Room:
#         """A room with information about the dimensions of its door and list of piano manufacturers it allows."""
#
#         def __init__(self, door_width, door_height, allowed_manufacturers):
#             """
#             Constructor.
#
#             :param door_width: The width of the room's door in centimeters.
#             :param door_height: The height of the room's door in centimeters.
#             :param allowed_manufacturers: The set of piano companies whose pianos are expected in this room.
#             """
#             self.door_width = door_width
#             self.door_height = door_height
#             self.allowed_manufacturers = allowed_manufacturers
#
#         def enter(self, piano):
#             """
#             Attempt to move a piano into this room and return a message of whether or not it succeeded.
#             The moving will succeed if the piano can fit through the door by turning it in any dimension by 90 degrees and
#             the manufacturer of the piano is in the set of allowed manufacturers.
#
#             Feedback message if successful: "Can move piano by <manufacturer>",
#             feedback message if unsuccessful: "Cannot move piano by <manufacturer>",
#             where <manufacturer> is the manufacturer of the piano.
#
#             :param piano: The piano being moved into this room.
#             :return: A feedback message.
#             """
#             if piano.manufacturer not in self.allowed_manufacturers:
#                 return f"Cannot move piano by {piano.get_manufacturer()}"
#
#             # Calculate minimum piano 2d size
#
#             if (piano.width <= self.door_height and piano.height <= self.door_width) or (
#                     piano.width <= self.door_width and piano.length <= self.door_height):
#                 return f"Can move piano by {piano.get_manufacturer()}"
#             else:
#                 return f"Cannot move piano by {piano.get_manufacturer()}"
#
#
#     if __name__ == '__main__':
#
#         assert camel_case_word_counter("answerIsFortyTwo") == 4
#         assert camel_case_word_counter("") == 0
#         assert camel_case_word_counter("kitty") == 1
#
#         assert search_backwards("hehehehehe", "h") == 6
#         assert search_backwards("hello", "h") == -1
#         assert search_backwards("hi", "e") == -1
#
#         assert beatles('Blackbird 1968') == "Blackbird is a Beatles song!"
#         assert beatles('Penny Lane 1967') == "Penny Lane is a Beatles song!"
#         assert beatles('Loveboat 1971') == "Loveboat is not a Beatles song!"
#
#         assert apple_sharing(10, 5) == 0
#         assert apple_sharing(3, 2) == 1
#         assert apple_sharing(4, 3) == 2
#
#         assert to_upper('hello', 'el') == 'hELLo'
#         assert to_upper('there', 'x') == 'there'
#         assert to_upper('there', 'rrr') == 'theRe'
#
#         assert lowercase_with_suffix("HELP", "FUL") == "HELPful"
#         assert lowercase_with_suffix("INVEST", "OR") == "INVEStor"
#         assert lowercase_with_suffix("AbC", "") == "abc"
#
#         assert remove_bigger_than_last([1, 2, 3, 4]) == [1, 2, 3, 4]
#         assert remove_bigger_than_last([1, 2, 4, 1]) == [1, 1]
#         assert remove_bigger_than_last([1, 2, 4, 0]) == [0]
#         assert remove_bigger_than_last([]) == []
#
#         assert multiplication(1, 8) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#         assert multiplication(0, 0) == {0: 0}
#         assert multiplication(4, -2) == {4: 16, 3: 9, 2: 4, 1: 1, 0: 0, -1: 1, -2: 4}
#
#         assert increment_by_one([6, 6, 8, 8]) == [7, 7, 9, 9]
#         assert increment_by_one([6, 6, 8, 8], pad_with_zeros=True) == [0, 7, 7, 9, 9, 0]
#         assert increment_by_one([-1, 2, 2], pad_with_zeros=False) == [0, 3, 3]
#
#         # assert fizz(3) is None
#
#         assert histogram("0") == ['**********'] + [''] * 9
#         assert histogram("123212") == ['', '*' * 6, '*' * 10, '*' * 3] + [''] * 6
#         assert histogram("") == [''] * 10
#         assert histogram("1234567890112") == ['***', '**********', '******', '***', '***', '***', '***', '***', '***',
#                                               '***']
#         assert histogram("0220") == ['*' * 10, '', '*' * 10] + [''] * 7
#         assert histogram("111111111112") == ['', '*' * 10] + [''] * 8
#
#         assert substring("hello", 2) == "he"
#         assert substring("hi", 2) == "hi"
#         assert substring("house", -1) == ""
#         # ============= BUS 1 =============
#
#         bus1 = Bus(["Station 1", "Station 2", "Station 3"], 5)
#
#         assert bus1.get_amount_of_people() == 1  # Bus driver is always in the bus!
#         assert bus1.get_current_station() == "Station 1"
#
#         assert bus1.register_new_passenger()
#         assert bus1.move_next()
#
#         assert bus1.get_current_station() == "Station 2"
#         for _ in range(4):
#             assert bus1.register_new_passenger()
#
#         assert bus1.get_amount_of_people() == 6
#         assert bus1.register_new_passenger() is False, "5"
#         assert bus1.move_next()
#
#         assert bus1.get_current_station() == "Station 3"
#         assert bus1.move_next() is False
#
#         # ============= BUS 2 =============
#
#         bus2 = Bus(["A", "B", "C", "D", "B", "A"], 10)
#
#         bus2.register_new_passenger()
#
#         assert bus2.get_current_station() == "A"
#
#         for _ in range(5):
#             assert bus2.move_next()
#
#         assert bus2.get_current_station() == "A"
#
#         # ============= BUS 3 =============
#
#         bus3 = Bus(["A", "B", "C", "D", "B", "A"], 3)
#
#         for _ in range(3):
#             assert bus3.register_new_passenger()
#
#         assert bus3.register_new_passenger() is False  # No more free seats
#         assert bus3.get_amount_of_people() == 4
#
#         for _ in range(4):
#             bus3.release_passenger()
#
#         assert bus3.get_amount_of_people() == 1  # Bus driver is always in the bus!
#
#         # ============ PIANO 1 ============
#         piano_yamaha = Piano(200, 205, 100, "Yamaha")
#
#         assert piano_yamaha.get_dimensions() == (200, 205, 100)
#         assert piano_yamaha.get_manufacturer() == "Yamaha"
#
#         # ============ PIANO 2 ============
#         piano_estonia = Piano(200, 200, 150, "Estonia Piano Factory")
#
#         assert piano_estonia.get_dimensions() == (200, 200, 150)
#         assert piano_estonia.get_manufacturer() == "Estonia Piano Factory"
#
#         # ============ ROOM  1 ============
#         room_yamaha = Room(100, 200, {"Yamaha"})
#
#         assert room_yamaha.enter(piano_yamaha) == "Can move piano by Yamaha"
#         assert room_yamaha.enter(piano_estonia) == "Cannot move piano by Estonia Piano Factory"
#
#         # ============ ROOM  2 ============
#         room_both = Room(120, 250, {"Yamaha", "Estonia Piano Factory"})
#
#         assert room_both.enter(piano_yamaha) == "Can move piano by Yamaha"
#         assert room_both.enter(piano_estonia) == "Cannot move piano by Estonia Piano Factory"