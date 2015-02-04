from django.db import models

# Create your models here.
class event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True, help_text="Describe your group")
    location = models.TextField(help_text="What can people put into maps to get to your house")
    members = models.ManyToManyField(users)
    alergies = models.TextField(blank=True, null=True)
    pics = models.ImageField(upload_to='photos', blank=True, null=True)

    def __str__(self):
        return self.name