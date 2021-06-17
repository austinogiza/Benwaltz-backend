from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    number= models.CharField(max_length=200, blank=False, null=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    feel = models.CharField(max_length=200)
    number= models.CharField(max_length=200)
    rating= models.CharField(max_length=200)
    recommend= models.CharField(max_length=200, blank=False, null=True)
    suggest= models.CharField(max_length=200)
    social= models.CharField(max_length=200)
    comment = models.TextField()
    photo = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name ="Reviews"
        verbose_name_plural = "Reviews"
