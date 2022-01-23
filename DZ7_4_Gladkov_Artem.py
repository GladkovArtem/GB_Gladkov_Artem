def dir_size_files(folder):
    import os
    list_size = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            path_file = os.path.abspath(f'{root}\{file}')
            list_size.append(os.stat(path_file).st_size)
    lest_len_size = []
    for i in list_size:
        lest_len_size.append(len(str(i)))
    result = {}
    for i in range(min(lest_len_size), max(lest_len_size)+1):
        k = lest_len_size.count(i)
        result['1'.zfill(i+1)[::-1]] = k
    print(result)
    return

dir_size_files('some_data')
