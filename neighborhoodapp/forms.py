from django import forms
from .models import Neighborhood,Business, Profile,Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NewNeighborhoodForm(forms.ModelForm):
    class Meta:
        model=Neighborhood
        fields=['name','image','description','location','count']
class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude =('user',)
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email', 'id_no','profile_pic']
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude =('user',)
    
    