from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200,null=True)
    message = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name