from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    # CharField has one required argument 'max_length'
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    # By using 'ForeignKey', we indicate that 'author' field is one instance or
    # record of 'User' model.
    # 'on_delete=CASCADE' means if the author is deleted, then the
    # post associated with the author should be deleted too.
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
