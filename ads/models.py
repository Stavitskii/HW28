from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pictures')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'



    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return self.name

