from django.db import models

# Create your models here.
class Affiliation(models.Model):
    departement = models.CharField(max_length=200)
    option = models.CharField(max_length=300)

class Participant(models.Model):
    Email = models.EmailField(unique=True)
    

class Fssbook(models.Model):
    title = models.CharField(max_length=200)
    localisation = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    desciption = models.TextField()
    image = models.ImageField(upload_to='images')
    affiliation = models.ForeignKey(Affiliation, on_delete=models.CASCADE)
    Participant = models.ManyToManyField(Participant,blank=True, null=True)
    admin_mail = models.EmailField()
    date = models.DateField(blank=True, null=True)