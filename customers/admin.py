# admin file allows us to have crud access to database

from django.contrib import admin
from customers.models import Customer

admin.site.register(Customer)
