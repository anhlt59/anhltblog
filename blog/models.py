from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse_lazy

# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published")
    )

    author = models.ForeignKey(User, related_name="blog_posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=120)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True) # every object added
    updated = models.DateTimeField(auto_now=True) # every object saved
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("blog:post_detail", args=[self.id, self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# @receiver(pre_save, sender=Post)
# def pre_save_slug(sender, *a, **kw):
#     import pdb; pdb.set_trace()
#     print(a)
#     print(kw)
    # slug = slugify(kw["slug"])
    # kw["slug"] = slug
