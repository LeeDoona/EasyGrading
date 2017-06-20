from django.db import models
from django import forms
from django.conf import settings
from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User
from account.models import PrivateMessage#, Publication

# from django.forms.extras.widgets import Select, SelectDateWidget


class PrivateMessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMessage
        fields = ['from_address', 'title', 'text']
        labels = {
            'from_address': 'From',
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name': TextInput(attrs={'class': u'form-control','placeholder': u'Enter First Name', 'required': True}),
            'last_name': TextInput(attrs={'class': u'form-control','placeholder': u'Enter Last Name', 'required': True}),
            'email': TextInput(attrs={'class': u'form-control','placeholder': u'Enter Email', 'required': True}),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name is not None and first_name is not '':
            return first_name
        else:
            raise forms.ValidationError("Cannot be blank")

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if last_name is not None and last_name is not '':
            return last_name
        else:
            raise forms.ValidationError("Cannot be blank")

    def clean_email(self):
        email = self.cleaned_data['email']
        if email is not None and email is not '':
            return email
        else:
             raise forms.ValidationError("Cannot be blank")

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        
        # Verify no duplicate emails occur.
        try:
            email = cleaned_data.get("email")
            user = User.objects.get(email=email)
            if user != self.instance:
                raise forms.ValidationError("Email already exists")
        except User.DoesNotExist:
            pass
#         
# class PublicationForm(forms.ModelForm):
#     class Meta:
#         model = Publication
#         fields = ['publication_id', 'title', 'description', 'file']
#         labels = {
#             'file': 'PDF',
#     }
# 
#     # Function will apply validation on the 'file' upload column in the table.
#     def clean_file(self):
#         upload = self.cleaned_data['file']
#         content_type = upload.content_type
#         if content_type in ['application/pdf']:
#             if upload._size <= 20971520:
#                 return upload
#             else:
#                 raise forms.ValidationError("Cannot exceed 20MB size")
#         else:
#             raise forms.ValidationError("Only accepting PDF files for course notes.")

