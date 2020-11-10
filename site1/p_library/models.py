from django.db import models


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class PublishingHouse(models.Model):
    name = models.TextField()
    phone = models.CharField(max_length=16)
    email = models.EmailField(null=True)
    city = models.TextField(null=True)
    foundation_date = models.SmallIntegerField(null=True)
    country = models.CharField(max_length=2)
    works = models.NullBooleanField()

    def __str__(self):
        return self.name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    p_house = models.ForeignKey(PublishingHouse, on_delete=models.SET_NULL, null=True)
    copy_count = models.SmallIntegerField(default=1)
    price = models.FloatField()

    def __str__(self):
        return self.title
