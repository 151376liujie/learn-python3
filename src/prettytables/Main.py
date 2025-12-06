from prettytable import PrettyTable
import random
import this

if __name__ == '__main__':
    table = PrettyTable()
    table.title = 'pretty table'
    table.field_names = ['name', 'age', 'sex', 'addr']

    x = [chr(ord('a') + i) for i in range(26)]
    print(x[9])
    for i in range(10):
        table.add_row((x[random.randint(0, len(x) - 1)], random.randint(0, 100), random.choice(['f', 'm']), 'beijing'))
    print(table)
