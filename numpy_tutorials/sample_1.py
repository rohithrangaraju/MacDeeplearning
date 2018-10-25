import pandas as pd
import numpy as np
import queue
import timeit

raw_data = {
    'SPC_Process_ID': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],
    'TaskID': [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    'Status': ['c', 'i', 'c', 'c', 'i', 'c', np.NaN, 'c', 'i', 'c', np.NaN, 'c', 'i', 'c', 'c', 'i', 'c', np.NaN],
    'C_ID': [np.NaN, np.NaN, 2, np.NaN, 3, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 6,
             np.NaN,
             np.NaN, np.NaN]

}
df = pd.DataFrame(raw_data, columns=['SPC_Process_ID', 'TaskID', 'Status', 'C_ID'])
sample_dict = dict()
start_time = timeit.timeit()
wanted_roots = [1, 5]
wanted_child = []
for rootId in set(df.get('SPC_Process_ID')):
    if rootId in wanted_roots or (wanted_child is not [] and rootId in wanted_child):
        print(rootId)
        dataFrame = df[df['SPC_Process_ID'] == rootId]  # taking root part of dataFrame
        status_list = list(dataFrame['Status'].values)
        child_IDs = list(dataFrame['C_ID'].unique())
        cleaned_child_IDs = [int(x) for x in child_IDs if str(x) != 'nan']
        sample_dict[rootId] = {'root_id': rootId, 'status': status_list, 'child_list': cleaned_child_IDs}
        wanted_child = wanted_child.__add__(sample_dict[rootId]['child_list'])
current_time = timeit.timeit()
print('Building the tree', current_time - start_time)
print(sample_dict)
q = queue.Queue()
count_dict = {}
root_ids = [1, 5]
main_count = {}
current_root = None
start_time = timeit.timeit()
for i in root_ids:
    current_root = i
    q.put(i)  # Inserting the root node
    while not q.empty():  # Performing  a level order traversal
        process_data = q.get()  # Extracting the first element from the queue
        process_data_dict = sample_dict[process_data]
        for i in process_data_dict['status']:
            try:  # Below statements will perform the count of the status from each node
                count_dict[i] += 1
            except KeyError:
                count_dict[i] = 1

        for i in process_data_dict['child_list']:  # Inserting the current nodes in the main queue.
            q.put(i)
    main_count[current_root] = count_dict
    count_dict = {}
# Now you have all the status count in count_dict variable
current_time = timeit.timeit()
print('Traversing the tree', current_time)
print(main_count)
