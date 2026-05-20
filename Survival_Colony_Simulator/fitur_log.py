import data_pusat
from struktur_node import SingleNode, DoubleNode, CircularNode

# SINGLE LINKED LIST
# Menambahkan activity log
def add_single_log(text):
    new_node = SingleNode(text)

    if data_pusat.log_head is None:
        data_pusat.log_head = new_node
    else:
        current = data_pusat.log_head

        while current.next:
            current = current.next

        current.next = new_node

# Menampilkan activity log
def show_single_log():
    current = data_pusat.log_head

    print("\n========== LOG AKTIVITAS ==========")

    while current:
        print("-", current.data)
        current = current.next

    print("==================================")

# DOUBLE LINKED LIST
# Menambahkan log ke double linked list
def add_double_log(text):
    new_node = DoubleNode(text)

    if data_pusat.double_head is None:
        data_pusat.double_head = data_pusat.double_tail = new_node
    else:
        data_pusat.double_tail.next = new_node
        new_node.prev = data_pusat.double_tail
        data_pusat.double_tail = new_node

# Menampilkan log dari depan
def show_double_forward():
    current = data_pusat.double_head

    print("\n====== DOUBLE LINKED LIST FORWARD ======")

    while current:
        print(current.data)
        current = current.next

    print("========================================")

# Menampilkan log dari belakang
def show_double_backward():
    current = data_pusat.double_tail

    print("\n====== DOUBLE LINKED LIST BACKWARD ======")

    while current:
        print(current.data)
        current = current.prev

    print("=========================================")

# CIRCULAR LINKED LIST
# Menambahkan survivor ke circular list
def add_circular_survivor(survivor):
    new_node = CircularNode(survivor)

    if data_pusat.circular_head is None:
        data_pusat.circular_head = new_node
        new_node.next = new_node
    else:
        current = data_pusat.circular_head

        while current.next != data_pusat.circular_head:
            current = current.next

        current.next = new_node
        new_node.next = data_pusat.circular_head

# Menampilkan giliran survivor
def show_circular_survivor():
    if data_pusat.circular_head is None:
        print("\nBelum ada Survivor")
        return

    print("\n====== GILIRAN SURVIVOR ======")

    current = data_pusat.circular_head

    while True:
        print(current.survivor.nama)
        current = current.next

        if current == data_pusat.circular_head:
            break

    print("===========================")
