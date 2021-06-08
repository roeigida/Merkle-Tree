# Tomer Shay, 323082701, Roei Gida, 322225897
import hashlib

user_input = ""
merkle_tree = []


class Node:

    def __init__(self, data):
        self.data = hashlib.sha256(data.encode('utf-8')).hexdigest()


def case1():
    global merkle_tree, user_input
    merkle_tree.append(Node(user_input[0]))


def root_calc():
    global merkle_tree
    if len(merkle_tree) == 0:
        return
    root_array = merkle_tree.copy()
    while len(root_array) > 1:
        temp = []
        is_odd = bool(len(root_array) % 2)
        pairs_num = int(len(root_array) / 2)
        for i in range(0, pairs_num):
            temp.append(Node(str(root_array[2 * i].data) + str(root_array[2 * i + 1].data)))

        if is_odd:
            temp.append(root_array[len(root_array) - 1])
        root_array = temp.copy()

    return root_array[0].data


def case2():
    print(root_calc())


def case3():
    global merkle_tree, user_input
    if len(merkle_tree) == 0:
        return
    print(root_calc(), end=" ")
    leaf_num = int(user_input[0])
    root_array = merkle_tree.copy()
    while len(root_array) > 1:
        if leaf_num % 2 == 0:
            if leaf_num != len(root_array) - 1:
                print("1" + root_array[leaf_num + 1].data, end=" ")
        else:
            print("0" + root_array[leaf_num - 1].data, end=" ")

        temp = []
        is_odd = bool(len(root_array) % 2)
        pairs_num = int(len(root_array) / 2)
        for i in range(0, pairs_num):
            temp.append(Node(str(root_array[2 * i].data) + str(root_array[2 * i + 1].data)))

        if is_odd:
            temp.append(root_array[- 1])
        root_array = temp.copy()
        leaf_num = int(leaf_num / 2)
    print("")


def case4():
    global user_input
    current_hash = hashlib.sha256(user_input[0].encode('utf-8')).hexdigest()
    for i in range(2, len(user_input)):
        if user_input[i] != "":
            if user_input[i][0] == '1':
                hash_chaining = str(current_hash) + str(user_input[i][1:])
            elif user_input[i][0] == '0':
                hash_chaining = str(user_input[i][1:]) + str(current_hash)
            else:
                print(False)
                return
            current_hash = hashlib.sha256(hash_chaining.encode('utf-8')).hexdigest()

    print(current_hash == user_input[1])


def case5():
    print("5")


def case6():
    print("6")


def case7():
    print("7")


def case8():
    print("8")


def case9():
    print("9")


def case10():
    print("10")


def case11():
    print("11")


# Press the green button in the gutter to run the script.
is_init = 0
cases = {
    1: 'case1',
    2: 'case2',
    3: 'case3',
    4: 'case4',
    5: 'case5',
    6: 'case6',
    7: 'case7',
    8: 'case8',
    9: 'case9',
    10: 'case10',
    11: 'case11'
}
while True:
    # Get input from user and Split parameters according to space
    user_input = input().split(" ")
    case = user_input[0]
    user_input = user_input[1:]
    # if not case.isnumeric() or int(case) < 0 or int(case) > 11:
    #     exit(0)
    eval(cases[int(case)] + "()")
