
def create_header(num_recorder, buffer_list):
    
    header = ['frame', 'error']

    for i in buffer_list:
        for j in range(1, num_recorder+1):
            reclabel = 'recorder' + str(j) + '_' + i
            header.append(reclabel)

    return(header)

#HOW TO USE
# num_recorder = 4
# buffer_list = ['1m', '3m', '6m', '9m']

# header = create_header(num_recorder, buffer_list)
# print(header)