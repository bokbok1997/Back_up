def rental_book(name,book_num):
    decrease_book(book_num)
    print(f'{name}님이 {book_num}권의 책을 대여하였습니다.')
    pass

number_of_book = 100

def decrease_book(book):
    global number_of_book
    number_of_book-=book
    print(f'남은 책의 수 : {number_of_book}')
    return number_of_book

rental_book('홍길동',3)