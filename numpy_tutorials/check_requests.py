# coding=utf-8

import queue

data = {1: {'process_id': 1, 'status': 'abc', 'child_list': [2]},
        2: {'process_id': 2, 'status': 'abc', 'child_list': []}}

q = queue.Queue()
count_dict = {}
q.put(1)  # Inserting the root node
while not q.empty():  # Performing  a level order traversal
    process_data = q.get()  # Extracting the first element from the queue
    process_data_dict=data[process_data]
    try:  # Below statements will perform the count of the status from each node
        count_dict[process_data_dict['status']] += 1
    except KeyError:
        count_dict[process_data_dict['status']] = 1

    for i in process_data_dict['child_list']:  # Inserting the current nodes in the main queue.
        q.put(i)

# Now you have all the status count in count_dict variable
print(count_dict)
