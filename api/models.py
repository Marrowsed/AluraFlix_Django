from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    color = models.CharField(max_length=10, null=False, blank=False)

    @property
    def has_videos(self):
        category = Category.objects.all()
        for c in category:
            name = [item.category.title for item in c.video_set.all()]
            return name

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Categorie"


class Video(models.Model):
    livre, created = Category.objects.get_or_create(title="LIVRE", color="red")
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    url = models.URLField(max_length=200, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=livre.id, null=False, blank=False, related_name='videos')


    def __str__(self):
        return self.title
