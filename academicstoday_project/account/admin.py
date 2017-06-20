from django.contrib import admin
from account.models import PrivateMessage
from account.models import Student
from account.models import Teacher
# from publisher.models import Publication

admin.site.register(PrivateMessage)
admin.site.register(Student)
admin.site.register(Teacher)
# admin.site.register(Publication)