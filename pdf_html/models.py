from django.db import models

class Profile(models.Model):
   name = models.CharField(max_length = 50)
   file = models.FileField(upload_to = 'media')

   class Meta:
      db_table = "media"