# models is the representation of out data. it is another word for database tables
# django works with SQL db
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)
    industry = models.CharField(max_length=100)
