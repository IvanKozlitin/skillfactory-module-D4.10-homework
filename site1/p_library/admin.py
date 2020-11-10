from django.contrib import admin
from .models import (Book, Author, PublishingHouse)


# [admin.site.register(item) for item in (Book, Author)]

# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#
#     @staticmethod
#     def author_full_name(obj):
#         return obj.author.full_name
#
#     list_display = ('title', 'author_full_name',)
#     fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('copy_count',)
    # fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'copy_count')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    pass
