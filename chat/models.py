from django.db import models
from django.utils.text import slugify


class Room(models.Model):
    title = models.CharField(max_length = 50, unique=True)
    slug  = models.SlugField(max_length = 100, unique=True, allow_unicode=True)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title, allow_unicode=True)
        return super().save()
    
    def __str__(self):
        return f'{self.pk}'
