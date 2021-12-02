from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    alt_text = models.CharField(max_length=255, blank=True)
    # description = models.TextField(max_length=200)
    # upload_date = models.DateTimeField(auto_now_add=True)
    # owner = models.ForeignKey('auth.User', related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.alt_text 
