from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=150)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title=models.CharField(max_length=150)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Note(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    content=models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    tags=models.ManyToManyField(Tag,blank=True)
    is_pinned=models.BooleanField(default=False)
    is_archived=models.BooleanField(default=False)
    is_trashed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def duplicate(self):
        old_tags=self.tags.all()
        self.pk=None
        self.title=f'${self.title} (Copy)'
        self.save()
        self.tags.set(old_tags)
        return self
    
    def __str__(self):
        return self.title
