from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Image Storage path
fs = FileSystemStorage(location='/media/articles/photos')

# list / choices declaration and definition
# start here

CATEGORY_LIST = (
    ('general', 'General'),
    ('beauty', 'Beauty'),
    ('trends', 'Trends'),
    ('travel', 'Travel'),
    ('fashion', 'Fashion'),
    ('culture', 'Culture'),
    ('food', 'Food'),
    ('entrepreneur', 'Entrepreneur'),
    ('fashion-pictorial', "Fashion Pictorial"),
    ('health', 'Health'),
    ('mens-corner', 'Men'),
    ('lifestyle', 'Lifestyle'),
)

PUBLISH_LIST = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

# list / choices declaration and definition
# end here

class Issue(models.Model):
    issue_id = models.CharField("Issue Number", max_length=10, null=False, blank=False, unique=True, primary_key=True)
    issue_pub_date = models.DateTimeField("Issue Publication Date", default=timezone.now)
    issue_status = models.CharField("Issue Status", choices=PUBLISH_LIST, default='draft', max_length=10)

class Magazine(models.Model):
    mag_issue = models.ForeignKey(Issue, on_delete=models.CASCADE, primary_key=True,)
    magazine_id = models.CharField("Magazine Name", max_length=10, null=False, blank=False)
    mag_date1 = models.DateField("Magazine Date")
    mag_date2 = models.DateField("Magazine Date")

class Category(models.Model):
    category_name = models.CharField(choices=CATEGORY_LIST, default='general',)
    category_description = models.TextField(max_length=3000)
    category_image = models.ImageField(storage=fs, blank=False, null=False)

class Article(models.Model):
    article_id = models.CharField("Article ID", max_length=10, null=False, blank=False, unique=True)
    header_image = models.ImageField("Head Image", storage=fs, blank=False, null=False)
    title = models.CharField("Article Title", max_length=10)
    summary = models.CharField("Article Summary", max_length=50, null=False, blank=False)
    body = models.TextField("Article Body", blank=False, null=False)
    body_image = models.ImageField("Article Image", storage=fs, blank=True, null=True)
    slug = models.SlugField(max_length=20, unique=True)
    article_issue = models.ForeignKey(Issue)
    author = models.ForeignKey(User)
    article_status = models.CharField("Issue Status", choices=PUBLISH_LIST, default='draft', max_length=10)
    publish_date = models.DateTimeField("Issue Publication Date", default=timezone.now)
    category = models.ForeignKey(Category)