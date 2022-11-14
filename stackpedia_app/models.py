from django.db import models
import uuid
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from profiles.models import UserProfile

# Create your models here.
class Post(models.Model):
    writer = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='img')
    content = RichTextField()
    post_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)
    category_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)

    def __str__(self):
        return self.title   