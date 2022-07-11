from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.base import ModelBase


class CustomModelBase(ModelBase):

    def __new__(mcs, name, bases, attrs):
        base = super(CustomModelBase, mcs).__new__(mcs, name, bases, attrs)
        for key, value in attrs.items():
            setattr(mcs, key, value)
        return base


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)


class Editor(models.Model):
    name = models.CharField(max_length=128)
    bestselling_author = models.ForeignKey(Author, models.CASCADE)


class Book(models.Model):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)
    editor = models.ForeignKey(Editor, models.CASCADE, related_name="edited_books")

    class Meta(metaclass=CustomModelBase):
        default_related_name = "books"
        ordering = ('title',)
        is_digit = ('title',)
