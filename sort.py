def bubble_sort(number_list:list, direction:str='ASC'):
    if direction not in ['ASC', 'DESC']:
        return
    number_list_length = len(number_list)
    for n in range(number_list_length):
        for s in range(number_list_length - n - 1):
            if direction == 'ASC':
                if number_list[s] > number_list[s + 1]:
                    save = number_list[s]
                    number_list[s] = number_list[s+1]
                    number_list[s+1] = save
            elif direction == 'DESC':
                if number_list[s] < number_list[s + 1]:
                    save = number_list[s]
                    number_list[s] = number_list[s+1]
                    number_list[s+1] = save



values = [1,8,-44,-66,-100,100,120,1,22,0,55,10,-1000,0,0,0,22,-22]

bubble_sort(values, 'ASC')
bubble_sort(values, 'DESC')

print(values)