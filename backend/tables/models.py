from django.db import models
from django.contrib.auth import get_user_model


class Table(models.Model):
    title = models.CharField(
        max_length=256,
    )
    description = models.TextField()
    header_image = models.ImageField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='tables',
    )
    game = models.CharField(max_length=256)
    start_date = models.DateTimeField()

    def __str__(self):
        return self.title
