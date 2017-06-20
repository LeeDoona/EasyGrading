from django.db import models
from django.contrib.auth.models import User

# from registrar.models import PeerReview
# from django.conf import settings
# from django.core.validators import MinValueValidator, MaxValueValidator
# import os


class PrivateMessage(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=127)
    text = models.TextField()
    sent_date = models.DateField(auto_now_add=True, null=True)
    to_address = models.CharField(max_length=255)
    from_address = models.CharField(max_length=255)
    
    def __str__(self):
        return "From: " + self.from_address + " To: " + self.to_address + " Title: " + self.title
    
    class Meta:
        db_table = 'at_private_messages'


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    
    def __str__(self):
        return self.user.first_name + " " + \
                          self.user.last_name 
    
    class Meta:
        db_table = 'at_students'


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    
    def __str__(self):
        return self.user.first_name + " " + \
            self.user.last_name + " "
    
    class Meta:
        db_table = 'at_teachers'
        
        
        
# class Publication(models.Model):
#     publication_id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=127, null=True)
#     description = models.TextField(null=True)
#     published_date = models.DateField(auto_now= True, null=True)
#     file = models.FileField(upload_to='uploads', null=True)
#     author = models.ForeignKey(User)
#     reviews = models.ManyToManyField(PeerReview)
#     
#     def delete(self, *args, **kwargs):
#         if self.file:
#             if os.path.isfile(self.file.path):
#                 os.remove(self.file.path)
#         super(Publication, self).delete(*args, **kwargs) # Call the "real" delete() method
#     
#     def __str__(self):
#         return self.title
# 
#     class Meta:
#         db_table = 'at_publications'