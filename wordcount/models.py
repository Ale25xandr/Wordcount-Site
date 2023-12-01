from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='path')


class Words(models.Model):
    word = models.TextField()
    count = models.IntegerField()
    file = models.ForeignKey(File, on_delete=models.CASCADE)
