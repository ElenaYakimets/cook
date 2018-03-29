def read_chefs_list(file_name):
    chefs_list = {}
    with open(file_name,encoding='cp1251') as chefs_list_file:
        for dish in chefs_list_file:
            dish = dish.encode('cp1251').decode('utf-8').strip().lower()
            print( dish )
            chefs_list[dish] = list()
            for line in range(int(chefs_list_file.readline())):
                ingredients = chefs_list_file.readline().encode('cp1251').decode('utf-8').split(' | ')
                chefs_list[dish].append({
                    'ingredient_name': ingredients[0].strip().lower(),
                    'quantity': int(ingredients[1].strip()),
                    'measure': ingredients[2].strip().lower()})
    return chefs_list


def get_purchase_sheet_by_dishes(person_count, dishes):
    purchase_sheet = {}
    chefs_list = read_chefs_list("cookbook.txt")
    for dish in dishes:
        for ingredient in chefs_list[dish]:
            new_purchase_sheet_item = dict(ingredient)
            new_purchase_sheet_item['quantity'] *= person_count
            if new_purchase_sheet_item['ingredient_name'] not in purchase_sheet:
                purchase_sheet[new_purchase_sheet_item['ingredient_name']] = new_purchase_sheet_item
            else:
                purchase_sheet[new_purchase_sheet_item['ingredient_name']]['quantity'] += \
                    new_purchase_sheet_item['quantity']
    return purchase_sheet


def print_purchase_sheet(purchase_sheet):
    full_purchase_sheet = []
    for purchase_sheet_item in purchase_sheet.values():
        full_purchase_sheet.append('{ingredient_name} {quantity} {measure}'.format(**purchase_sheet_item))
    for purchase_sheet_item in sorted(full_purchase_sheet):
        print(purchase_sheet_item)


def create_purchase_sheet():
    person_count = int(input("Введите количество человек: "))
    dishes = input("Введите названия блюд: ").lower().split(", ")
    purchase_sheet = get_purchase_sheet_by_dishes(person_count, dishes)
    print_purchase_sheet(purchase_sheet)


create_purchase_sheet()