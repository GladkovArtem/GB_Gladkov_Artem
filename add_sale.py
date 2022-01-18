def add_sale(argv):
    program, *sale = argv
    with open('bakery.csv ', 'a', encoding='utf-8') as f:
        f.write(f'{sale}\n')
    return None

if __name__ == '__main__':
   import sys
   exit(add_sale(sys.argv))