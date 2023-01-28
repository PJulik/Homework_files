from pprint import pprint
def get_shop_list_by_dishes(dishes, person_count):
    with open('data.txt', encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            dish = line.strip()
            dish_count = int(f.readline())
            ingredients = []
            for i in range(dish_count):
                ingredient = f.readline().strip()
                name, quantity, measure = ingredient.split(' | ')
                ingredients.append({
                    'name': name,
                    'quantity': quantity,
                    'measure': measure
                })
            f.readline()
            cook_book[dish] = ingredients
    pprint(cook_book, sort_dicts=False, width=100)
    print()

    shop_list_by_dishes = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingredients in cook_book[dish]:
                ingr = ingredients['name']
                if ingr in shop_list_by_dishes.keys():
                    shop_list_by_dishes[ingr]['quantity'] += int(ingredients['quantity']) * person_count
                else:
                    meas = ingredients['measure']
                    shop_list_by_dishes[ingr] = {'quantity': int(ingredients['quantity']) * person_count,
                                                'measure': meas}
    return shop_list_by_dishes

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))