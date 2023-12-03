cook_book = {}
def readrecipe():
    cook_book = {}
    with open ('recipe.txt') as f:
        count = 0
        for line in f:
            if line.strip() == "":
                count = 0
            else:
                if count == 0:
                    cook_book [line.strip()] = []
                elif count>1:
                    last_key = list(cook_book.keys())[-1]
                    ingredient = line.strip().split(" | ")
                    cook_book [last_key].append({'ingredient_name':ingredient[0],'quantity':ingredient[1],'measure':ingredient[2] })
                count += 1
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
           for  ingredient in cook_book [dish]:
                if ingredient["ingredient_name"] in shop_list:
                    shop_list [ingredient["ingredient_name"]] ["quantity"] = shop_list [ingredient["ingredient_name"]] ["quantity"] + (int(ingredient["quantity"]) * person_count)
                else:
                    shop_list [ingredient["ingredient_name"]] = {"measure":ingredient["measure"],"quantity":int(ingredient["quantity"]) * person_count}
    return shop_list

cook_book = readrecipe()
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)