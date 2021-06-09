# Tomer Shay, 323082701, Roei Gida, 322225897
import base64
import hashlib

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key

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
    # generate public and private key and convert them to pem format
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
    pem_private = private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                            format=serialization.PrivateFormat.TraditionalOpenSSL,
                                            encryption_algorithm=serialization.NoEncryption()).decode()

    public_key = private_key.public_key()
    pem_public = public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                         format=serialization.PublicFormat.SubjectPublicKeyInfo).decode()
    print(pem_private)
    print(pem_public)


def case6():
    global user_input
    root_val = root_calc()
    input_key = ""
    for s in user_input:
        input_key += s + " "
    input_key = list(input_key)
    input_key[-1] = '\n'
    input_key = "".join(input_key)

    while user_input != "":
        user_input = input()
        input_key += user_input + '\n'

    key = load_pem_private_key(input_key.encode("utf-8"), password=None, backend=default_backend())
    root_signature = key.sign(root_val.encode("utf-8"), padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                                                                    salt_length=padding.PSS.MAX_LENGTH),
                              hashes.SHA256())
    print(base64.b64encode(root_signature).decode("utf-8"))


def case7():
    global user_input
    input_key = ""
    for s in user_input:
        input_key += s + " "
    input_key = list(input_key)
    input_key[-1] = '\n'
    input_key = "".join(input_key)

    while user_input != "":
        user_input = input()
        input_key += user_input + '\n'
    print("input_key" + input_key)
    user_input = input().split(" ")
    sign = user_input[0]
    verification_text = user_input[1]
    public_key = load_pem_public_key(input_key.encode(), backend=default_backend())
    try:
        public_key.verify(base64.decodebytes(sign.encode("utf-8")), verification_text.encode(),
                          padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
                          hashes.SHA256())
        print(True)
    except InvalidSignature:
        print(False)


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
