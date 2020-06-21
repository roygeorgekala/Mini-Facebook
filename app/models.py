from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class userinfo(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    birthday = models.DateField(default = now)
    gender = models.CharField(max_length=10, default='Male')
    about = models.CharField(max_length=200, default = " ")
    profile_pic = models.ImageField(upload_to='profile_pic/',default = None)
    cover_pic = models.ImageField(upload_to='cover_pic/')

    def __str__(self):
        return self.user.first_name

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user_info = models.ForeignKey(userinfo,on_delete=models.CASCADE)
    text = models.CharField(max_length=400,blank=True)
    photo = models.ImageField(upload_to='post_images/',null=True)
    video = models.FileField(upload_to='video_videos/',null = True)
    l = models.IntegerField(default=0)
    c = models.IntegerField(default=0)

    def __str__(self):
        return self.user.first_name

class likes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name

class Comments(models.Model):
        user = models.ForeignKey(User,on_delete=models.CASCADE)
        post = models.ForeignKey(Post,on_delete=models.CASCADE)
        body = models.CharField(max_length=100)

        def __str__(self):
            return self.user.first_name
