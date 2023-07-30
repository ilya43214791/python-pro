import uuid
from django.db import models
from ckeditor.fields import RichTextField


class TimeDataBaseModel:
    create = models.DateTimeField('Create', auto_now_add=True, null=True)
    update = models.DateTimeField('Update', auto_now=True, null=True)


class Tag(TimeDataBaseModel, models.Model):
    name = models.CharField(max_length=90, unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name


class Category(TimeDataBaseModel, models.Model):
    name = models.CharField("Товари", max_length=20, unique=True)
    description = RichTextField("Description")

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Good(TimeDataBaseModel, models.Model):
    name = models.CharField("Товари", max_length=20, unique=True)
    description = RichTextField("Description")
    price = models.FloatField("Ціна")
    active = models.FloatField("Active", default=False, help_text='Показувати або не показувати товар')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='goods')
    tags = models.ManyToManyField(Tag, related_name="goods")
    image = models.ImageField(upload_to='image', null=True, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} - {self.price}'


class ItemsDecor(TimeDataBaseModel, models.Model):
    name = models.CharField("Предмети для власного декору", max_length=50, unique=False)
    description = RichTextField("Description")
    price = models.FloatField("Ціна")
    active = models.FloatField("Active", default=False, help_text='Показувати або не показувати товар')

    def __str__(self):
        return self.name
