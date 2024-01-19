import json
from pprint import pprint


def book_info(book, categories):
    # 여기에 코드를 작성합니다.
    temp={
        "author" : book["author"],
        'categoryName' : book["categoryId"],
        'cover' : book["cover"],
        'description' : book["description"],
        'id' : book["id"],
        'priceSales' : book["priceSales"],
        'title' : book["title"]
        }
    gen_ids=book["categoryId"]
    for cat in categories_list:
        for i in range(len(book["categoryId"])):
            if cat['id'] == book["categoryId"][i]:
                temp['categoryName'][i]=cat['name']
    return temp


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
