def get_list(l, length):
    import get_error_free_int
    l = []
    print(l)
    for i in range(1, length+1):
        message = "Please enter the element of list   :    "
        element = get_error_free_int.get_int(message)
        l.append(element)

#print(get_list)
