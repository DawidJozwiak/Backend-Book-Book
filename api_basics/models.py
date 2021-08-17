from django.db import models

class User(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

# Create your models here.
class Publication(models.Model):
    ISN = models.IntegerField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    edition = models.SmallIntegerField()
    publicationYear = models.SmallIntegerField()
    description = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)

    def __str__(self):
        return self.ISN, self.title, self.author, self.publisher, self.edition, self.publicationYear, self.description, self.tags


class Users(models.Model):
    # id = models.IntegerField()
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    emailPrivate = models.CharField(max_length=100)
    emailPublic = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.id, self.name, self.surname, self.location, self.emailPrivate, self.emailPublic, self.password


class Shelves(models.Model):
    # id = models.IntegerField()
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name="shelf", blank=True, null=True)
    label = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    users_fk = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, default= 1)

    def __str__(self):
        return self.id, self.label, self.surname, self.location, self.users_fk
