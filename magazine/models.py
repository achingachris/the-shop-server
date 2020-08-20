from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User


# Author Models
class Author(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_name = models.CharField('Author Display Name', max_length=25, null=False, default="Author")


    class Meta:
        verbose_name = 'Authors'
        verbose_name_plural = verbose_name
    
    def __str__(self):
       return self.author_name
        
# Categories Models
class Category(models.Model):
    # list of required categories required
    CATEGORY_LIST = (
        ('beauty', 'Beauty'),
        ('trends', 'Trends'),
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
    category_link = models.SlugField(max_length=200, null=False, unique=True, default='artcle')

    class Meta:
        verbose_name = 'Category List'
        verbose_name_plural = verbose_name

    def __str__(self):
       return self.category

    @property
    def imageURL(self):
        try:
            url = self.cover_image.url
        except:
            url = ''
        return url



# Magazine Models
class Magazine(models.Model):
    cover_image = models.ImageField(upload_to='uploads/')
    mag_title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200, null=False)
    publish_date = models.DateField()
    magazine_link = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='uploads/')

    class Meta:
        verbose_name = "Magazine Issues"
        verbose_name_plural = verbose_name
    
    def __str__(self):
       return self.mag_title

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
    subheading = models.CharField(max_length=20, null=False)
    body = models.TextField()
    body_image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    magazine_issue = models.ForeignKey(Magazine, on_delete=models.SET_NULL, null=True, blank=True)
    published = models.CharField(choices=STATUS, default='draft', max_length=20)
    publish_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    article_link = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Article list"
        verbose_name_plural = verbose_name

    def __str__(self):
       return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.article_link})

# News Updates
class News(models.Model):
    title = models.CharField(max_length=20, null=False)
    image = models.ImageField(upload_to='uploads/')
    description = models.CharField(max_length=100, null=False)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    news_link = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = "News Updates"
        verbose_name_plural = verbose_name
    
    def __str__(self):
       return self.title

# subscriptions
class Subscription(models.Model):
    pass

# image gallery
class ImageGallery(models.Model):
    pass

# video gallery
class VideoGallery(models.Model):
    pass
