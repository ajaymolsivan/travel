from django.db import models

# Create your models here.c
from django.utils.safestring import mark_safe


class Banner(models.Model):
    image=models.ImageField(upload_to='banners')

    content=models.CharField(max_length=250)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
