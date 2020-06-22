from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    # CharField has one required argument 'max_length'
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    # By using 'ForeignKey' for field 'author' with model 'User', we indicate
    # the relationship between model Post and User is many posts belong to one
    # user.
    # 'on_delete=CASCADE' means if the user is deleted, then the
    # post associated with the user should be deleted too.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # auto_new_add=True will automatically set the field to now when the object
    # is first created.
    created_date = models.DateTimeField(auto_now_add=True)
    # auto_now=True will automatically set the field to now every time the
    # object is saved.
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    # since one post can belong to many category and one category can also
    # belong to many post, So we use 'ManyToMany' to define the relationship
    # between class Category and Post in terms of field 'posts'
    posts = models.ManyToManyField(Post, blank=True, related_name='categories')

    def __str__(self):
        return self.name

    # set the plural name for the class name, by default, Django will use name+'s'
    class Meta:
        verbose_name_plural = 'Categories'
