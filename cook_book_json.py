import json

#########################################################################
def get_cook_book_dict():
    with open('list_of_recipes.json', 'r') as f:
        
        cook_book = json.load(f)
        return cook_book

#########################################################################
def get_shop_list_by_dishes(dishes, person_count, cook_book):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)
      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

#########################################################################
def print_shop_list(shop_list):
  print('')
  for shop_list_item in shop_list.values():
    print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))
    
#########################################################################
def create_shop_list():
  person_count = int(input('Введите количество персон: '))
  dishes = input('Введите блюда через запятую: ').split(', ')
  cook_book = get_cook_book_dict()
  shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
  print_shop_list(shop_list)
  
#########################################################################
create_shop_list()

