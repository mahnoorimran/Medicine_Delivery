from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from products.models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['first_name','email','username','password1','password2']

        def __init__(self,*args,**kwargs):
            super(CustomUserCreationForm, self).__init__(*args,**kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'})

    def _init_(self,args,*kwargs):
        super(CustomUserCreationForm, self)._init_(args,*kwargs)

        self.fields['first_name'].widget.attrs.update({'id':'id_first_name'})
        self.fields['email'].widget.attrs.update({'id':'id_email'})
        self.fields['username'].widget.attrs.update({'id':'id_username'})
        self.fields['password1'].widget.attrs.update({'id':'id_password1'})
        self.fields['password2'].widget.attrs.update({'id':'id_password2'})
        


class UpCustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['first_name','email','username','password1','password2']

        def __init__(self,*args,**kwargs):
            super(UpCustomUserCreationForm, self).__init__(*args,**kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'})

    def _init_(self,args,*kwargs):
        super(UpCustomUserCreationForm, self)._init_(args,*kwargs)

        self.fields['first_name'].widget.attrs.update({'id':'id_first_name'})
        self.fields['email'].widget.attrs.update({'id':'id_email'})
        self.fields['username'].widget.attrs.update({'id':'id_username'})
        self.fields['password1'].widget.attrs.update({'id':'id_password1'})
        self.fields['password2'].widget.attrs.update({'id':'id_password2'})
        


class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=['name','username','email','location','bio','short_intro','profile_image']

    def __init__(self,*args,**kwargs):
        super(ProfileForm, self).__init__(*args,**kwargs)

        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['username'].widget.attrs.update({'class':'form-control'})
        self.fields['email'].widget.attrs.update({'class':'form-control'})
        self.fields['location'].widget.attrs.update({'class':'form-control'})
        self.fields['bio'].widget.attrs.update({'class':'form-control'})
        self.fields['short_intro'].widget.attrs.update({'class':'form-control'})
        self.fields['profile_image'].widget.attrs.update({'class':'btn btn-success'})

class CustForm(ModelForm):
    class Meta:
        model=Customer
        fields=['user','name','email']

    def __init__(self,*args,**kwargs):
        super(CustForm, self).__init__(*args,**kwargs)

        self.fields['user'].widget.attrs.update({'class':'form-control'})

        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['email'].widget.attrs.update({'class':'form-control'})

class UpdateCustForm(ModelForm):
    class Meta:
        model=Customer
        fields=['user','name','email']

    def __init__(self,*args,**kwargs):
        super(UpdateCustForm, self).__init__(*args,**kwargs)


        self.fields['user'].widget.attrs.update({'class':'form-control'})

        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['email'].widget.attrs.update({'class':'form-control'})
       
        
       