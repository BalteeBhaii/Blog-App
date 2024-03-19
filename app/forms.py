from django import forms
from app.models import Comments, Subscribe
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = {'content','name','email','website'}
    def __init__(self, *args, **kwargs): # this funciton help to edit the placeholder of fileds
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['placeholder'] = 'Type your comment...'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['website'].widget.attrs['placeholder'] = 'Website(optional)'

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields ='__all__'
        labels = {'email':('')}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Type email'

class NewUserForm(UserCreationForm): 
    # django provide build in UserCreation Form and that exists in djanog.contrib.auth
    class Meta:
        model = User
        fields = ("username","email","password1","password2",)

    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = "Type Username"
        self.fields['email'].widget.attrs['placeholder'] = "Type Email"
        self.fields['password1'].widget.attrs['placeholder'] = "Type Password"
        self.fields['password2'].widget.attrs['placeholder'] = "Type Confirm Password"


  # validation for register user
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username = username)
        if new.count():
            raise forms.ValidationError("User already exist")
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email = email)
        if new.count():
            raise forms.ValidationError("Email already exist")
        return email
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password not matched.")
        return password2