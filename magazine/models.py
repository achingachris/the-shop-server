from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Author Models
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# Categories Models
class Category(models.Model):
    # list of required categories required
    CATEGORY_LIST = (
        ('beauty', 'Beauty'),
        ('trends', 'Travel'),
        ('travel', 'Travel'),
        ('fashion', 'Fashion'),
        ('culture', 'Culture'),
        ('food', 'Food'),
        ('entrepreneur', 'Entrepreneur'),
        ('fashion-pictorial', 'Fashion Pictorial'),
        ('health', 'Health'),
        ('men', 'Mens Corner'),
        ('lifestyle', 'Lifestyle'),
        ('general', 'General')
    )
    category = models.CharField('Category Name', choices=CATEGORY_LIST, default='general')
    cover_image = models.ImageField()
    description = models.TextField()
    category_link = models.SlugField()

# Article Model
class Article(models.Model):
    pass

# Magazine Models
class Magazine(models.Model):
    pass

# News Updates
class News(models.Model):
    pass

# subscriptions
class Subscription(models.Model):
    pass

# image gallery
class ImageGallery(models.Model):
    pass

# video gallery
class VideoGallery(models.Model):
    pass
