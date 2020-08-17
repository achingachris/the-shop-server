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

# Magazine Models
class Magazine(models.Model):
    cover_image = models.ImageField()
    title = models.CharField()
    description = models.CharField()
    magazine_link = models.SlugField()
    image1 = models.ImageField()
    image2 = models.ImageField()

# Article Model
class Article(models.Model):
    # article status
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    cover_image = models.ImageField()
    title = models.CharField()
    subtitle = models.CharField()
    description = models.CharField()
    subheading1 = models.CharField()
    body1 = models.TextField()
    subheading2 = models.CharField()
    body2 = models.TextField()
    subheading3 = models.CharField()
    body3 = models.TextField()
    body_image = models.ImageField()
    category = models.ForeignKey(Category)
    magazine_issue = models.ForeignKey(Magazine)
    published = models.CharField(choices=STATUS, default='draft')
    publish_date = models.DateField()
    author = models.ForeignKey(Author)
    article_link = models.SlugField()

# News Updates
class News(models.Model):
    title = models.CharField()
    image = models.ImageField()
    description = models.CharField()
    body = models.TextField()
    category = models.ForeignKey(Category)
    date = models.DateField()
    news_link = models.SlugField()

# subscriptions
class Subscription(models.Model):
    pass

# image gallery
class ImageGallery(models.Model):
    pass

# video gallery
class VideoGallery(models.Model):
    pass
