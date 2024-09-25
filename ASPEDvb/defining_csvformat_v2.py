
def create_header(num_recorder, buffer_list):
    # first column
    header = ['frame']

    for i in buffer_list:
        for j in range(1, num_recorder+1):
            # column for ped count within each buffer of each recorder
            reclabel = 'recorder' + str(j) + '_' + i

            header.append(reclabel)

    for i in buffer_list:
        for j in range(1, num_recorder+1):
            # column to indicate 'view', 'partial view' of the frame
            view = 'view_recorder' + str(j) + '_' + i 

            header.append(view)

    return(header)

# #HOW TO USE
# num_recorder = 4
# buffer_list = ['1m', '3m', '6m', '9m']

# header = create_header(num_recorder, buffer_list)
# print(header)