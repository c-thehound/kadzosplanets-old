from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=300,blank=True, null=True)
    mugshot = models.ImageField()
    email = models.EmailField(null=True,blank=True)
    title = models.CharField(max_length=300,null=True,blank=True)
    facebook = models.CharField(max_length=200,blank=True, null=True)
    instagram = models.CharField(max_length=200,blank=True, null=True)
    twitter = models.CharField(max_length=200,blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class WeeksTheme(models.Model):
    text = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.text

class KadzosTagline(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

class Logo(models.Model):
    image = models.ImageField(upload_to="logos",blank=False, null=True)

    def __str__(self):
        return str(self.pk)

class Message(models.Model):
    email = models.EmailField(blank=False, null=False)
    message = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.email+" says "+self.message