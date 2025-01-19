from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, default='')
    slug = models.SlugField(
        max_length=250,
        unique_for_date='pub_date' # now we can't have two posts with the same slug in the same date
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='blog/posts/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )

    objects = models.Manager()
    published = PublishedManager()
    
    class Meta:
        ordering = ['-pub_date']
        indexes = [
            models.Index(fields=['-pub_date'])
        ]
        db_table = 'posts'
    
    def __str__(self):
        return self.title
    
    @property
    def local_pub_date(self):
        return timezone.localtime(self.pub_date)
    
    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[
                self.local_pub_date.year,
                self.local_pub_date.month,
                self.local_pub_date.day,
                self.slug
            ]
        )
    