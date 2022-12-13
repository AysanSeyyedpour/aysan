from django.db import models
import uuid

# Create your models here.

class student(models.Model):

    id = models.UUIDField(primary_key=True, default = uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class content(models.Model):

    id = models.UUIDField(primary_key=True, default = uuid.uuid4, unique=True,  editable=False)
    description = models.TextField(null=True, blank=True, max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.description)


class course(models.Model):

    id = models.UUIDField(primary_key=True,default = uuid.uuid4, unique=True,  editable=False)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    contents = models.ManyToManyField(content)

    def __str__(self):
        return str(self.name)


class registration(models.Model):

    id = models.UUIDField(primary_key=True, default = uuid.uuid4, unique=True,  editable=False)
    created = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(course, on_delete=models.CASCADE)
    student = models.ForeignKey(student, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.course)


