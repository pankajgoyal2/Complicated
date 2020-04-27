def get_int(input_message):
    num = input(input_message)
    try:
       return int(num)
    except:
        return get_int(input_message)
