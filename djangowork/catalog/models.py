from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField("Товари", max_length=20, unique=True)
    description = RichTextField("Description")

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField("Товари", max_length=20, unique=True)
    description = RichTextField("Description")
    price = models.FloatField("Ціна")
    active = models.FloatField("Active", default=False, help_text='Показувати або не показувати товар')

    def __str__(self):
        return f'{self.name} - {self.price}'


class ItemsDecor(models.Model):
    name = models.CharField("Предмети для власного декору", max_length=50, unique=False)
    description = RichTextField("Description")
    price = models.FloatField("Ціна")
    active = models.FloatField("Active", default=False, help_text='Показувати або не показувати товар')

    def __str__(self):
        return self.name
