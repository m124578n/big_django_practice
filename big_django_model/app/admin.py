from django.contrib import admin

from .models import Person, Group, Membership, Product, Publisher, Book
# Register your models here.

admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Product)
admin.site.register(Publisher)
admin.site.register(Book)
