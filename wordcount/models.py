from django.db import models


class Words(models.Model):
    word = models.TextField(unique=True)
    count = models.IntegerField()


class File(models.Model):
    file = models.FileField(upload_to='path')
    words = models.ForeignKey(Words, on_delete=models.CASCADE, auto_created=True)




