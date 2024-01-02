from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.name
    

class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, default='')
    publisher = models.ForeignKey(Publisher, on_delete = models.CASCADE, related_name='books')
    add_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
## 设置related_name前：publisher.book_set.all
## 设置related_name后：publisher.books.all



## -------------------------------------------------------------------------------------
## many to many example
    
class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)



## -------------------------------------------------------------------------------------
## 自定義 Manager
    
# First, define the Manager subclass.
# class DahlBookManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(author='Roald Dahl')

# # Then hook it into the Book model explicitly.
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=50)

#     objects = models.Manager() # The default manager.
#     dahl_objects = DahlBookManager() # The Dahl-specific manager.



## -------------------------------------------------------------------------------------
from django.db import models
from django.urls import reverse
 
# 自定义Manager方法
class HighRatingManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(rating=1)

# CHOICES选项
class Rating(models.IntegerChoices):
    VERYGOOD = 1, 'Very Good'
    GOOD = 2, 'Good'
    BAD = 3, 'Bad'

class Product(models.Model):
    # 数据表字段
    name = models.CharField('name', max_length=30)
    rating = models.IntegerField(choices=Rating.choices)
 
    # MANAGERS方法
    objects = models.Manager()
    high_rating_products =HighRatingManager()
 
    # META类选项
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
 
    # __str__方法
    def __str__(self):
        return self.name
 
    # 重写save方法
    def save(self, *args, **kwargs):
        self.do_something()
        super().save(*args, **kwargs) 
        self.do_something_else()
 
    # 定义单个对象绝对路径
    def get_absolute_url(self):
        return reverse('product_details', kwargs={'pk': self.id})
 
    # 其它自定义方法
    def do_something(self):
        pass

    def do_something_else(self):
        pass