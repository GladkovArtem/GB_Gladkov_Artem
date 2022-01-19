def show_sales(argv):
    if len(argv)==1:
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            for i in f:
                print(f'{i[2:len(i)-3]}')

    elif len(argv)==2:
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            for index, line in enumerate(f,1):
                if index>=int(argv[1]):
                    print(f'{line[2:len(line) - 3]}')

    elif len(argv)==3:
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            for index, line in enumerate(f,1):
                if index>=int(argv[1]) and index<=int(argv[2]):
                    print(f'{line[2:len(line) - 3]}')
    else:
        print('incorrect params')
    return None

if __name__ == '__main__':
   import sys
   exit(show_sales(sys.argv))

