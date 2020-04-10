def split(input_str):
    length = len(input_str)
    i_start = 0
    i_end = 0


    while True:
        if input_str[i_end] == ' ':
            one_word = input_str[i_start:i_end]
        elif input_str[i_end] == '\\':
            if input_str[i_end+1] == 'n':
                print('换行')
            elif input_str[i_end+1] == 't':
                print('制表符')
