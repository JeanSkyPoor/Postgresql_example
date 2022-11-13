def read_data_for_table():
    with open('data.txt', 'r') as f:
            fast_list=[]
            for line in f:
                fast_list.append(line.strip('\n'))
            
            return fast_list