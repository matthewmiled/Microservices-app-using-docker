from django.db import models

# Create your models here.

# TO MIGRATE, MAKE SURE YOU WRITE THE MIGRATE COMMAND WITHIN THE DOCKER CONTAINER
# docker-compose exec backend sh  -> python3 manage.py migrate
# Otherwise it will not be able to connect to the mysql database

class BlogPost(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

class BlogPostUser(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()

    models.UniqueConstraint('user_id', 'product_id', name='user_product_unique')

    