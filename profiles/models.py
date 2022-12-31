from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    username = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    profilePic = models.ImageField(upload_to='img', blank=True, null=True,
                                   default='assets/default-profile-pic.jpeg')
    profileBanner = models.ImageField(upload_to='img', blank=True, null=True, default='assets/default-banner.png')
    about = models.TextField()
    profile_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    @property
    def get_photo_url(self):
        if self.profilePic and hasattr(self.profilePic, 'url'):
            return self.profilePic.url
        else:
            return "/static/assets/default-profile-pic.jpeg"

    @property
    def get_banner_url(self):
        if self.profileBanner and hasattr(self.profileBanner, 'url'):
            return self.profileBanner.url
        else:
            return "/static/assets/default-banner.png"

    @property
    def get_profile_name(self):
        username = self.user
        return username
