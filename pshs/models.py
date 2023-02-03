from django.db import models



class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()


    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

class Attendance(models.Model):
    name = models.CharField(max_length= 20)
    lib_room = models.IntegerField()
    lib_num = models.IntegerField()
    class_num = models.IntegerField()
    location = models.CharField(max_length=20)
    check_time = models.DateTimeField()

class Recurit(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    create_date = models.DateTimeField()

'''class Apply(models.Model):
    recurit = models.ForeignKey(Recurit, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    clsss_num = models.IntegerField()
    email = models.TextField()
'''

class Assembly(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    content = models.TextField()
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)


class Apply(models.Model):
    recurit = models.ForeignKey(Recurit, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

# Create your models here.
