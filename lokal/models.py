from django.db import models

# Create your models here.


class Local(models.Model):
    tytul = models.TextField(help_text='Nazwa lokalu')
