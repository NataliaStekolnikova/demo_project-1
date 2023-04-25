# Name: str
# Price: float
# Quantity: int

import json

def main():
    items = list() #items = []

    while True:
        print('Please, enter new item data  (exit to finish)')
        print('.......................................')

        name = input('Please, enter item name: ')
        if name == 'exit':
            break

        try:
            price = float(input('Please, enter item Price: '))
            quantity = int(input('Please, enter item Quantity: '))
        except ValueError:
            print('Please, enter valid values for price and quantity!')
            continue

        item = {'name': name, 'price': price, 'quantity': quantity, }
        items.append(item)

    with open('db.json', 'r', encoding='utf-8') as file:
        content = json.load(file)

    with open('db.json', 'w') as file:
        json.dump(content + items, file)


if __name__ == '__main__':
    main()
