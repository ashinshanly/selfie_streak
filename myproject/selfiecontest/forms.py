<<<<<<< HEAD
from django import forms

from .models import Profile,Picto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class ContactForm(forms.Form):
    full_name=forms.CharField()
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('college', 'city', 'pic',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class EntryForm(forms.ModelForm):
    class Meta:
        model = Picto
        fields = ('user','image_caption','image')
=======
from django import forms

from .models import Profile,Picto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('college', 'city', 'pic',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class EntryForm(forms.ModelForm):
    class Meta:
        model = Picto
        fields = ('user','image_caption','image')
>>>>>>> 659e0f3b84863e77d7b53cdb048a235845dd8167
