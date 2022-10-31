from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    color = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Categorie"


class Video(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    url = models.URLField(max_length=200, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1, null=False, blank=False)

    def __str__(self):
        return self.title
