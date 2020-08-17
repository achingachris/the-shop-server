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
    category = models.CharField('Category Name', choices=CATEGORY_LIST, default='general', max_length=20)
    cover_image = models.ImageField(upload_to='uploads/')
    description = models.TextField(max_length=250, null=False)
    category_link = models.SlugField(max_length=25)

# Magazine Models
class Magazine(models.Model):
    cover_image = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200, null=False)
    publish_date = models.DateField()
    magazine_link = models.SlugField(max_length=25, unique_for_date='publish_date')
    image = models.ImageField(upload_to='uploads/')

    # @property
	# def imageURL(self):
    #         try:
    #             url = self.image.url
    #         except:
    #             url = ''
    #         return url

# Article Model
class Article(models.Model):
    # article status
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    cover_image = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=20, null=False)
    subtitle = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200, null=False)
    subheading1 = models.CharField(max_length=20, null=False)
    body1 = models.TextField()
    subheading2 = models.CharField(max_length=20, null=False)
    body2 = models.TextField()
    subheading3 = models.CharField(max_length=20, null=False)
    body3 = models.TextField()
    body_image = models.ImageField(upload_to='uploads/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    magazine_issue = models.ForeignKey(Magazine, on_delete=models.SET_NULL, null=True, blank=True)
    published = models.CharField(choices=STATUS, default='draft', max_length=20)
    publish_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    article_link = models.SlugField(max_length=25, unique_for_date='publish_date')

# News Updates
class News(models.Model):
    title = models.CharField(max_length=20, null=False)
    image = models.ImageField(upload_to='uploads/')
    description = models.CharField(max_length=100, null=False)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    news_link = models.SlugField(max_length=25, unique_for_date='date')

    # @property
	# def imageURL(self):
	# 	try:
	# 		url = self.image.url
	# 	except:
	# 		url = ''
	# 	return url

# subscriptions
class Subscription(models.Model):
    pass

# image gallery
class ImageGallery(models.Model):
    pass

# video gallery
class VideoGallery(models.Model):
    pass
