from django import template

register = template.Library()


@register.filter(name='p_house_and_book')
def p_house_and_book(book, p_house):
    if book.p_house.id == p_house.id:
        return book
    return None
