from django.db import models

# Create your models here.
class Teams(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now=True)

    # This will correct the verbose spelling in Django admin to the correct\ plural spelling of Teams
    class Meta:
        verbose_name_plural = 'Teams'

    # function in class
    # was angezeigt werden soll statt Teams object (1)
    def __str__(self):
        return self.first_name



