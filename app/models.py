from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    # In django they provide inbuilt model called user and that user have a filed like name email passowrd etc
    # but User model have not a profile image or slug or bio so we created another model called Proifle and that
    # Profile model linked with User model with one to one and we add some more fileds in Profile model. That is the reaosn to created that model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
    slug = models.SlugField(max_length=200, unique=True)
    bio = models.CharField(max_length=200)
 
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.user.username)
        return super(Profile, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.user.first_name

class Subscribe(models.Model):
    email = models.EmailField(max_length=100)
    date = models.DateField(auto_now=True)
    

class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)


    def save(self, *args, **kwargs): # to generate slug automaitcally
        if not self.id:
            self.slug = slugify(self.name)
        return super(Tag, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    tags = models.ManyToManyField(Tag, blank=True, related_name='post')
    view_count = models.IntegerField(null=True, blank=True)
    is_featured = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    bookmarks = models.ManyToManyField(User, related_name="bookmarks", default="None", blank=True)
    likes = models.ManyToManyField(User,related_name="post_likes", default="None",blank=True)

    #count no of likes
    def number_of_likes(self):
        return self.likes.count()

    
class Comments(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now=True) 
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='replies')


class WebsiteMeta(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    about = models.TextField()

